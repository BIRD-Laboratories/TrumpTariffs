import re
from pypdf import PdfReader

# Define the pattern for subchapter codes
subchapter_pattern = re.compile(r'^\d{4}\.\d{2}\.\d{2}')

# Subchapter data for China
subchapter_data = {
    "9903.88.01": {"rate": 25, "value": 34},
    "9903.88.15": {"rate": 7.5, "value": 300},
    "9903.88.04": {"rate": 25, "value": 200},
    "9903.88.03": {"rate": 25, "value": 16},
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

def calculate_average_tariff_rate(combined_data, total_import_value):
    """
    Calculate the overall average and weighted average tariff rates.
    """
    rates = [data['rate'] for data in combined_data.values()]
    average_rate = sum(rates) / len(rates) if rates else 0.0
    
    total_value_weighted_rate = sum(data['rate'] * data['value'] for data in combined_data.values())
    if total_import_value > 0:
        weighted_average_rate = total_value_weighted_rate / total_import_value
    else:
        weighted_average_rate = 0.0
    
    return average_rate, weighted_average_rate

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

def calculate_expected_tax_revenue(weighted_average_rate, taxable_amount):
    """
    Calculate the expected tax revenue.
    """
    return (weighted_average_rate / 100) * taxable_amount

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
    domestic_goods_value = get_total_import_value("Domestic Goods")
    total_consumption = get_total_consumption()
    
    # Update Canada and Mexico data with user input values
    canada_data["CANADA.ALL"]["value"] = total_import_value_canada
    mexico_data["MEXICO.ALL"]["value"] = total_import_value_mexico
    
    # Extract tariff data for China
    code_frequency_china = extract_tariff_data(pdf_path_china, "China", total_import_value_china)
    
    # Combine all tariff data
    combined_data = {}
    combined_data.update(subchapter_data)
    combined_data.update(canada_data)
    combined_data.update(mexico_data)
    
    # Calculate total import value from all countries
    total_import_value = total_import_value_china + total_import_value_canada + total_import_value_mexico
    
    # Check if imports + domestic goods exceed total consumption
    if total_import_value + domestic_goods_value > total_consumption:
        print("Error: Imports and domestic goods exceed total consumption.")
        return
    
    # Calculate average and weighted average tariff rates
    average_rate, weighted_average_rate = calculate_average_tariff_rate(combined_data, total_import_value)
    print(f"\nAverage Tariff Rate: {average_rate:.2f}%")
    print(f"Weighted Average Tariff Rate: {weighted_average_rate:.2f}%")
    
    # Calculate tariff contribution
    tariff_contribution = (weighted_average_rate / 100) * total_import_value
    
    # Calculate net inflation impact
    price_decrease = 5.0  # Assumed 5% price decrease
    net_inflation_impact = calculate_inflation_impact(tariff_contribution, total_consumption, price_decrease)
    print(f"\nNet Inflation Impact: {net_inflation_impact:.2f}%")
    
    # Calculate expected tax revenue
    tax_revenue = calculate_expected_tax_revenue(weighted_average_rate, total_import_value)
    print(f"\nTotal Expected Tax Revenue: ${tax_revenue:.2f}")

if __name__ == '__main__':
    main()
