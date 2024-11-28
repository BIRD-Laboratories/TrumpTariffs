import re
from pypdf import PdfReader

# Define the pattern for subchapter codes
subchapter_pattern = re.compile(r'^\d{4}\.\d{2}\.\d{2}')

# Subchapter data for China with rates in decimal
subchapter_data = {
    "9903.88.01": {"rate": 0.25, "value": 34},
    "9903.88.15": {"rate": 0.075, "value": 300},
    "9903.88.04": {"rate": 0.25, "value": 200},
    "9903.88.03": {"rate": 0.25, "value": 16},
}

# Placeholder codes for Canada and Mexico with flat tariff rates in decimal
canada_data = {
    "CANADA.ALL": {"rate": 0.0, "value": 0},  # Rate and value to be set based on user input
}

mexico_data = {
    "MEXICO.ALL": {"rate": 0.0, "value": 0},  # Rate and value to be set based on user input
}

# Define impact factors for each country on CPI
country_cpi_impact = {
    "China": 0.0886,  # Impact factor on CPI
    "Mexico": 0.02851,  # Impact factor on CPI
    "Canada": 0.19648,  # Impact factor on CPI
}

def extract_tariff_data(pdf_path, country, total_import_value):
    """
    Extract subchapter codes and their frequencies from the PDF for China.
    """
    code_frequency = {}
    if country.lower() != "china":
        return code_frequency
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return code_frequency
    
    lines = text.split("\n")
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(' ', 1)
        if len(parts) >= 2:
            subheading = parts[0]
            code = parts[1]
            if code in subchapter_data:
                if code in code_frequency:
                    code_frequency[code] += 1
                else:
                    code_frequency[code] = 1
    return code_frequency

def calculate_weighted_average_tariff_rate(data, total_import_value):
    """
    Calculate the weighted average tariff rate.
    """
    total_tariff_contribution = 0
    total_value = sum(details['value'] for details in data.values())
    
    for code, details in data.items():
        proportion = details['value'] / total_value if total_value != 0 else 0
        adjusted_value = proportion * total_import_value
        tariff_contribution = details['rate'] * adjusted_value
        total_tariff_contribution += tariff_contribution
    
    weighted_average_rate = total_tariff_contribution / total_import_value if total_import_value != 0 else 0
    return weighted_average_rate

def get_input(country, input_type):
    """
    Generic function to get input values for countries.
    """
    while True:
        try:
            if input_type == 'import_value':
                value = float(input(f"Enter the total consumption value from {country} (in dollars): "))
                if value < 0:
                    print("Import value cannot be negative.")
                else:
                    return value
            elif input_type == 'tariff_rate':
                rate = float(input(f"Enter the tariff rate for {country} (as a decimal, e.g., 0.10 for 10%): "))
                if 0 <= rate <= 1:
                    return rate
                else:
                    print("Tariff rate must be between 0 and 1.")
            else:
                print("Invalid input type.")
                return None
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_extra_tariff_rate_china():
    """
    Prompt the user to input the extra tariff rate for China.
    """
    while True:
        try:
            rate = float(input("Enter the extra tariff rate for China (as a decimal, e.g., 0.05 for 5%): "))
            if 0 <= rate <= 1:
                return rate
            else:
                print("Extra tariff rate must be between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_extra_cpi_value_adjusted(china_n, canada_n, mexico_n, china_tariff, canada_tariff, mexico_tariff):
    """
    Calculate the extra CPI rate based on impact factors and tariff rates.
    """
    sum_n = china_n + canada_n + mexico_n
    term1 = 1 - sum_n
    term2 = (china_n * (1 + china_tariff)) + (canada_n * (1 + canada_tariff)) + (mexico_n * (1 + mexico_tariff))
    extra_cpi_rate = term1 + term2
    return extra_cpi_rate

def calculate_extra_cpi_weight_adjusted(proportion_china, proportion_canada, proportion_mexico, china_tariff, canada_tariff, mexico_tariff):
    """
    Calculate the extra CPI rate based on the proportion of imports and tariff rates.
    """
    sum_proportion = proportion_china + proportion_canada + proportion_mexico
    term1 = 1 - sum_proportion
    term2 = (proportion_china * (1 + china_tariff)) + (proportion_canada * (1 + canada_tariff)) + (proportion_mexico * (1 + mexico_tariff))
    extra_cpi_rate = term1 + term2
    return extra_cpi_rate

def main():
    # Paths to PDF files for China
    pdf_path_china = 'tariff_table_china.pdf'
    
    # Get total import values for each country
    total_import_value_china = get_input("China", 'import_value')
    total_import_value_canada = get_input("Canada", 'import_value')
    total_import_value_mexico = get_input("Mexico", 'import_value')
    
    # Get tariff rates for Canada and Mexico
    canada_data["CANADA.ALL"]["rate"] = get_input("Canada", 'tariff_rate')
    mexico_data["MEXICO.ALL"]["rate"] = get_input("Mexico", 'tariff_rate')
    
    # Get extra tariff rate for China
    extra_tariff_rate_china = get_extra_tariff_rate_china()
    
    # Get total consumption
    total_consumption = get_input("USA", 'import_value')
    
    # Calculate domestic goods value
    total_import_value = total_import_value_china + total_import_value_canada + total_import_value_mexico
    domestic_goods_value = total_consumption - total_import_value
    
    # Check if total imports exceed total consumption
    if total_import_value > total_consumption:
        print("Error: Total imports exceed total consumption.")
        return
    
    # Update Canada and Mexico data with user input values
    canada_data["CANADA.ALL"]["value"] = total_import_value_canada
    mexico_data["MEXICO.ALL"]["value"] = total_import_value_mexico
    
    # Extract tariff data for China
    code_frequency_china = extract_tariff_data(pdf_path_china, "China", total_import_value_china)
    
    # Calculate weighted tariff rate for China
    weighted_tariff_rate_china = calculate_weighted_average_tariff_rate(subchapter_data, total_import_value_china)
    
    # Add extra tariff rate to China's weighted tariff rate
    weighted_tariff_rate_china += extra_tariff_rate_china
    
    # Use flat tariff rates for Canada and Mexico
    weighted_tariff_rate_canada = canada_data["CANADA.ALL"]["rate"]
    weighted_tariff_rate_mexico = mexico_data["MEXICO.ALL"]["rate"]
    
    # Retrieve impact factors
    china_n = country_cpi_impact["China"]
    canada_n = country_cpi_impact["Canada"]
    mexico_n = country_cpi_impact["Mexico"]
    
    # Calculate proportions for weight-adjusted version
    proportion_china = total_import_value_china / total_consumption
    proportion_canada = total_import_value_canada / total_consumption
    proportion_mexico = total_import_value_mexico / total_consumption
    
    # Calculate Extra CPI (Value Adjusted)
    extra_cpi_value_adjusted = calculate_extra_cpi_value_adjusted(china_n, canada_n, mexico_n, weighted_tariff_rate_china, weighted_tariff_rate_canada, weighted_tariff_rate_mexico)
    print(f"\nExtra CPI (Value Adjusted): {extra_cpi_value_adjusted:.4f}")
    
    # Calculate Extra CPI (Weight Adjusted)
    extra_cpi_weight_adjusted = calculate_extra_cpi_weight_adjusted(proportion_china, proportion_canada, proportion_mexico, weighted_tariff_rate_china, weighted_tariff_rate_canada, weighted_tariff_rate_mexico)
    print(f"\nExtra CPI (Weight Adjusted): {extra_cpi_weight_adjusted:.4f}")
    
    # Additional calculations and outputs can be added here if needed

if __name__ == '__main__':
    main()
