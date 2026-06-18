
import pandas as pd
import numpy as np

print("Series from List:")
print(pd.Series([10, 20, 30, 40, 50]))

print("\nSeries from NumPy Array:")
print(pd.Series(np.array([100, 200, 300, 400, 500])))

print("\nSeries from Dictionary:")
print(pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
