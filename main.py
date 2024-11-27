import re
from pypdf import PdfReader

# Define the pattern for subchapter codes
subchapter_pattern = re.compile(r'^\d{4}\.\d{2}\.\d{2}')

# Subchapter data for China
subchapter_data = {
    "9903.88.01": {"rate": 35, "value": 34},
    "9903.88.15": {"rate": 17.5, "value": 300},
    "9903.88.04": {"rate": 35, "value": 200},
    "9903.88.03": {"rate": 35, "value": 16},
}

# Placeholder codes for Canada and Mexico with flat tariff rates
canada_data = {
    "CANADA.ALL": {"rate": 25, "value": 0},  # Value to be set based on user input
}

mexico_data = {
    "MEXICO.ALL": {"rate": 25, "value": 0},  # Value to be set based on user input
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
        tariff_contribution = (details['rate'] / 100) * adjusted_value
        total_tariff_contribution += tariff_contribution
    
    weighted_average_rate = (total_tariff_contribution / total_import_value) * 100 if total_import_value != 0 else 0
    return weighted_average_rate

def get_total_import_value(country):
    """
    Prompt the user to input the total import value for a specified country.
    """
    while True:
        try:
            value = float(input(f"Enter the total import value from {country} (in dollars): "))
            if value < 0:
                print("Import value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_total_consumption():
    """
    Prompt the user to input the total consumption of the USA.
    """
    while True:
        try:
            value = float(input("Enter the total consumption of the USA (in dollars): "))
            if value <= 0:
                print("Total consumption must be a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_expected_tax_revenue(weighted_average_rate, total_import_value):
    """
    Calculate the expected tax revenue.
    """
    return (weighted_average_rate / 100) * total_import_value

def calculate_inflation_impact(tariff_contribution, total_consumption, price_decrease):
    """
    Calculate the net inflation impact considering tariff contribution and price decrease.
    """
    inflation_impact = (tariff_contribution / total_consumption) * 100
    net_inflation_impact = inflation_impact - price_decrease
    return net_inflation_impact

def main():
    # Paths to PDF files for China
    pdf_path_china = 'tariff_table_china.pdf'
    
    # Get total import values
    total_import_value_china = get_total_import_value("China")
    total_import_value_canada = get_total_import_value("Canada")
    total_import_value_mexico = get_total_import_value("Mexico")
    total_consumption = get_total_consumption()
    
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
    
    # Print code_frequency
    print("Code Frequency:", code_frequency_china)
    
    # Calculate mean tariff value
    total_value = 0
    total_goods = sum(code_frequency_china.values())
    for code, freq in code_frequency_china.items():
        total_value += freq * subchapter_data[code]['value']
    if total_goods > 0:
        mean_value = total_value / total_goods
        print("Mean Tariff Value: ${:.2f}".format(mean_value))
    else:
        print("No tariffed goods found.")
    
    # Combine all tariff data
    combined_data = {}
    combined_data.update(subchapter_data)
    combined_data.update(canada_data)
    combined_data.update(mexico_data)
    
    # Calculate weighted average tariff rate for all imports
    weighted_average_rate = calculate_weighted_average_tariff_rate(combined_data, total_import_value)
    print(f"\nWeighted Average Tariff Rate (All Countries): {weighted_average_rate:.2f}%")
    
    # Calculate weighted average tariff rate for China only
    weighted_average_rate_china = calculate_weighted_average_tariff_rate(subchapter_data, total_import_value_china)
    print(f"Weighted Average Tariff Rate (China Only): {weighted_average_rate_china:.2f}%")
    
    # Calculate tariff contribution
    tariff_contribution = calculate_expected_tax_revenue(weighted_average_rate, total_import_value)
    
    # Calculate net inflation impact with an assumed price decrease of 5%
    price_decrease = 5.0
    net_inflation_impact = calculate_inflation_impact(tariff_contribution, total_consumption, price_decrease)
    print(f"\nNet Inflation Impact: {net_inflation_impact:.2f}%")
    
    # Calculate expected tax revenue
    tax_revenue = calculate_expected_tax_revenue(weighted_average_rate, total_import_value)
    print(f"\nTotal Expected Tax Revenue: ${tax_revenue:.2f}")

if __name__ == '__main__':
    main()
