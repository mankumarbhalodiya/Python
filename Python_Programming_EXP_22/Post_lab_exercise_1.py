import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005],
    'ProductCategory': ['Electronics', 'Books', 'Apparel', 'Books', 'Electronics'],
    'Price': [499.99, 12.50, 75.00, 22.95, 1200.00],
    'UnitsSold': [5, 20, 15, 8, 3],
    'OrderDate': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'IsDiscounted': [True, False, True, False, True]
}

df = pd.DataFrame(data)

print("--- Original DataFrame Head (First 5 Rows) ---")
print(df.head())
print("\n" + "="*50 + "\n")

print("--- Column Data Types (Series output from .dtypes) ---")
column_data_types = df.dtypes
print(column_data_types)

print("\n" + "="*50 + "\n")
print("--- DataFrame Summary (.info() method) ---")
df.info()
