import pandas as pd
import numpy as np
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005],
    'ProductCategory': ['Electronics', 'Books', 'Apparel', 'Books', 'Electronics'],
    'Price': [499.99, 12.50, 75.00, 22.95, 1200.00],
    'UnitsSold': [5, 20, np.nan, 8, 3],   # Introduced a missing value here
    'OrderDate': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'IsDiscounted': [True, False, True, False, True]
}

df = pd.DataFrame(data)

print("--- DataFrame Head with Missing Value (Row Index 2) ---")
print(df.head())
print("\n" + "="*50 + "\n")

print("--- Column Data Types ---")
print(df.dtypes)
print("\n" + "="*50 + "\n")

mean_units_sold = df['UnitsSold'].mean()
print(f"Calculated Mean of 'UnitsSold': {mean_units_sold:.2f}")
df['UnitsSold'].fillna(mean_units_sold, inplace=True)

print("\n--- DataFrame after Imputing NaN with Mean ---")
print(df)
# The missing value at index 2 (originally NaN) is now filled with 9.00
# (Calculation: (5 + 20 + 8 + 3) / 4 = 36 / 4 = 9.0)
