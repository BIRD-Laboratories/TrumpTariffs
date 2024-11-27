import re
from pypdf import PdfReader

# Define the pattern for subchapter codes
subchapter_pattern = re.compile(r'^\d{4}\.\d{2}\.\d{2}')

# Subchapter data mapping codes to tariff rates and value they affect
subchapter_data = {
    "9903.88.01": {"rate": 25, "value": 34},
    "9903.88.15": {"rate": 7.5, "value": 300},
    "9903.88.04": {"rate": 25, "value": 200},
    "9903.88.03": {"rate": 25, "value": 16},
}

def extract_tariff_data(pdf_path, total_import_value):
    """
    Extract subchapter codes and their frequencies from the PDF.

    Parameters:
    pdf_path (str): Path to the PDF file containing tariff data.
    total_import_value (float): Total import value in dollars.

    Returns:
    dict: Dictionary with subchapter code as key and frequency as value.
    """
    code_frequency = {}
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return code_frequency
    
    # Split the text into lines
    lines = text.split("\n")
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Split the line by the first space to separate subheading and code
        parts = line.split(' ', 1)
        if len(parts) >= 2:
            subheading = parts[0]
            code = parts[1]
            # Check if the code is in the subchapter_data
            if code in subchapter_data:
                if code in code_frequency:
                    code_frequency[code] += 1
                else:
                    code_frequency[code] = 1
    return code_frequency

def calculate_average_tariff_rate(subchapter_data, total_import_value):
    """
    Calculate the overall average and weighted average tariff rates.

    Parameters:
    subchapter_data (dict): Dictionary with subchapter code as key and dict of rate and value as value.
    total_import_value (float): Total import value in dollars.

    Returns:
    tuple: (average_rate, weighted_average_rate) in percentage.
    """
    # Calculate average rate
    rates = [data['rate'] for data in subchapter_data.values()]
    average_rate = sum(rates) / len(rates) if rates else 0.0
    
    # Calculate weighted average rate
    total_value_weighted_rate = sum(data['rate'] * data['value'] for data in subchapter_data.values())
    if total_import_value > 0:
        weighted_average_rate = total_value_weighted_rate / total_import_value
    else:
        weighted_average_rate = 0.0
    
    return average_rate, weighted_average_rate

def get_total_import_value():
    """
    Prompt the user to input the total import value from China.

    Returns:
    float: Total import value in dollars.
    """
    while True:
        try:
            value = float(input("Enter the total import value from China (in dollars): "))
            if value <= 0:
                print("Total import value must be a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_expected_tax_revenue(weighted_average_rate, taxable_amount):
    """
    Calculate the expected tax revenue.

    Parameters:
    weighted_average_rate (float): Weighted average tariff rate in percentage.
    taxable_amount (float): Total taxable import value in dollars.

    Returns:
    float: Expected tax revenue in dollars.
    """
    return (weighted_average_rate / 100) * taxable_amount

def main():
    pdf_path = 'tariff_table.pdf'  # Replace with the actual path to the PDF file
    total_import_value = get_total_import_value()
    code_frequency = extract_tariff_data(pdf_path, total_import_value)
    
    # Calculate original average and weighted average tariff rates
    average_rate, weighted_average_rate = calculate_average_tariff_rate(subchapter_data, total_import_value)
    print(f"\nOriginal Average Tariff Rate: {average_rate:.2f}%")
    print(f"Original Weighted Average Tariff Rate: {weighted_average_rate:.2f}%")
    
    # Calculate the taxable amount in the original scenario
    taxable_amount_original = total_import_value
    print(f"\nOriginal Taxable Amount: ${taxable_amount_original:.2f}")
    
    # Calculate expected tax revenue with original rates
    original_tax_revenue = calculate_expected_tax_revenue(weighted_average_rate, taxable_amount_original)
    print(f"\nOriginal Expected Tax Revenue: ${original_tax_revenue:.2f}")
    
    # Simulate adding 10% tariff on the entire import value
    additional_tax_revenue = 0.10 * total_import_value
    total_tax_revenue_sim = original_tax_revenue + additional_tax_revenue
    simulated_weighted_average_rate = weighted_average_rate + 10.0
    print(f"\nSimulated Weighted Average Tariff Rate (after adding 10%): {simulated_weighted_average_rate:.2f}%")
    
    # In simulation, taxable_amount is the total import value
    taxable_amount_sim = total_import_value
    print(f"\nSimulated Taxable Amount (after adding 10%): ${taxable_amount_sim:.2f}")
    
    # Calculate simulated expected tax revenue
    print(f"\nSimulated Expected Tax Revenue (after adding 10%): ${total_tax_revenue_sim:.2f}")

if __name__ == '__main__':
    main()
