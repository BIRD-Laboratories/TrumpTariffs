# TrumpTariffs

Brief foray into Trump Tariff data, blog post coming soon with more data. Proper citations soon as well.

## Usage 

```bash
pip install pypdf
python main.py
```

## Results(2019 Data USTR)
26 Nov Version
I mistakingly used all china imports. I meant to use only exports doing torwards the USA not everyone.

### Prototype
```
Enter the total import value from China (in dollars): 2070

Original Average Tariff Rate: 20.62%
Original Weighted Average Tariff Rate: 4.11%

Original Taxable Amount: $2070.00

Original Expected Tax Revenue: $85.00

Simulated Weighted Average Tariff Rate (after adding 10%): 14.11%

Simulated Taxable Amount (after adding 10%): $2070.00

Simulated Expected Tax Revenue (after adding 10%): $292.00
```

## Results(2018 Data USTR)
27 Nov Version

Total consumption is only durable goods, PCE also includes other things which aren't goods. Goods are from various sources including but not limited to USTR. Measured in billions of USD. 5% is subtracted because usually producers will eat some of the costs to stay competitive.

### Status Quo
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 326
Enter the total import value from Mexico (in dollars): 358
Enter the total consumption of the USA (in dollars): 1440
Code Frequency: {'9903.88.15': 2982, '9903.88.03': 5908, '9903.88.01': 865, '9903.88.04': 43}
Mean Tariff Value: $104.83

Weighted Average Tariff Rate (All Countries): 6.89%
Weighted Average Tariff Rate (China Only): 15.45%

Net Inflation Impact: 0.85%

Total Expected Tax Revenue: $84.31
```

### Trump Tariffs Plan Circa Nov 2024 
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 326
Enter the total import value from Mexico (in dollars): 358
Enter the total consumption of the USA (in dollars): 1440
Code Frequency: {'9903.88.15': 2982, '9903.88.03': 5908, '9903.88.01': 865, '9903.88.04': 43}
Mean Tariff Value: $104.83

Weighted Average Tariff Rate (All Countries): 25.20%
Weighted Average Tariff Rate (China Only): 25.45%

Net Inflation Impact: 16.42%

Total Expected Tax Revenue: $308.48
```

## Results(2018 Data USTR)

28 Nov Version

I updated it to properly weight durable goods.

### Status Quo
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 326
Enter the total import value from Mexico (in dollars): 358
Enter the total consumption of the USA (in dollars): 1440
Code Frequency: {'9903.88.15': 2982, '9903.88.03': 5908, '9903.88.01': 865, '9903.88.04': 43}
Mean Tariff Value: $104.83

Weighted Average Tariff Rate (All Countries): 6.89%
Weighted Average Tariff Rate (China Only): 15.45%

Net Inflation Impact: 0.73%

Total Expected Tax Revenue: $84.31
```

### Trump Tariffs Plan Circa Nov 2024 
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 326
Enter the total import value from Mexico (in dollars): 358
Enter the total consumption of the USA (in dollars): 1440
Code Frequency: {'9903.88.15': 2982, '9903.88.03': 5908, '9903.88.01': 865, '9903.88.04': 43}
Mean Tariff Value: $104.83

Weighted Average Tariff Rate (All Countries): 25.20%
Weighted Average Tariff Rate (China Only): 25.45%

Net Inflation Impact: 2.67%

Total Expected Tax Revenue: $308.48
```

## Results(2018 Data USTR)
28 Nov Version Updated 15:14 PST

I changed it to be profiled based on the goods that align with the country in the CPI. I had deepseek help me find this list. This is slightly more accruate in principle but for mexico and canada not all goods mentioned are exclusive to them. 

When finding the values the code no longer needs to be updated with the rate increases as they are asked.

The only issue is that it somewhat underrepresnts the issue from these tariffs. This assumes everything domestic has no ties with china, that china won't fight back etc. It doesn't get the point accross but this is the truth. 

I decide to have both methods, one assumes only these goods will go up and one assumes the whole catagory will. The real result will be somewhere in between.

### Status Quo
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 326
Enter the total import value from Mexico (in dollars): 358
Enter the tariff rate for Canada (as a decimal, e.g., 0.10 for 10%): 0
Enter the tariff rate for Mexico (as a decimal, e.g., 0.10 for 10%): 0
Enter the extra tariff rate for China (as a decimal, e.g., 0.05 for 5%): 0
Enter the total consumption value from USA (in dollars): 14000

Extra CPI (Value Adjusted): 1.0137

Extra CPI (Weight Adjusted): 1.0060
```

### Trump Tariffs Plan Circa Nov 2024 
```
Enter the total import value from China (in dollars): 540
Enter the total import value from Canada (in dollars): 325
Enter the total import value from Mexico (in dollars): 358
Enter the tariff rate for Canada (as a decimal, e.g., 0.10 for 10%): 25
Tariff rate must be between 0 and 1.
Enter the tariff rate for Canada (as a decimal, e.g., 0.10 for 10%): 0.25
Enter the tariff rate for Mexico (as a decimal, e.g., 0.10 for 10%): 0.25
Enter the extra tariff rate for China (as a decimal, e.g., 0.05 for 5%): 0.1
Enter the total consumption value from USA (in dollars): 14000

Extra CPI (Value Adjusted): 1.0788

Extra CPI (Weight Adjusted): 1.0220
```

## Results(2018 Data USTR)
29 Nov Version

To elimate income tax we'll either have to take a crazy deficit, hope DOGE actually works, or Trump Admin will not be able to cut as much as they wanted to.

### Status Quo
```
Enter the total consumption value from China (in dollars): 540
Enter the total consumption value from Canada (in dollars): 326
Enter the total consumption value from Mexico (in dollars): 358
Enter the tariff rate for Canada (as a decimal, e.g., 0.10 for 10%): 0
Enter the tariff rate for Mexico (as a decimal, e.g., 0.10 for 10%): 0
Enter the extra tariff rate for China (as a decimal, e.g., 0.05 for 5%): 0
Enter the total consumption value from USA (in dollars): 14000
Enter the total income tax revenue (in dollars): 1684

Extra CPI (Value Adjusted): 1.0137

Extra CPI (Weight Adjusted): 1.0060

Total Tariff Revenue: $83.45
Percentage of Tariff Revenue relative to Income Tax Revenue: 4.96%
```

### Trump Tariffs Plan Circa Nov 2024 
```
Enter the total consumption value from China (in dollars): 540
Enter the total consumption value from Canada (in dollars): 326
Enter the total consumption value from Mexico (in dollars): 358
Enter the tariff rate for Canada (as a decimal, e.g., 0.10 for 10%): 0.25
Enter the tariff rate for Mexico (as a decimal, e.g., 0.10 for 10%): 0.25
Enter the extra tariff rate for China (as a decimal, e.g., 0.05 for 5%): 0.1
Enter the total consumption value from USA (in dollars): 14000
Enter the total income tax revenue (in dollars): 1684

Extra CPI (Value Adjusted): 1.0788

Extra CPI (Weight Adjusted): 1.0220

Total Tariff Revenue: $308.45
Percentage of Tariff Revenue relative to Income Tax Revenue: 18.32%
```

## Improvement Ideas
Weight each country differently since china and mexico don't ship the same exact TYPES of goods.

Some specific catagories will be hit harder than others so just saying aggregete inflation is x% is not of much use.

Add taxes and percentage of income tax it will pay back to the calcuations
