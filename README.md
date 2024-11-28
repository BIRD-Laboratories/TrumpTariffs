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
