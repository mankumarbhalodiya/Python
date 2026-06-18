import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

print("Stacked Vertically:")
print(pd.concat([s1, s2]))

print("\nStacked Horizontally:")
print(pd.concat([s1, s2], axis=1))