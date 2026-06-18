import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 4, 5, 6])

print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

print("\nAddition of Series:")
print(s1 + s2)

print("\nSubtraction of Series:")
print(s1 - s2)

print("\nMultiplication of Series:")
print(s1 * s2)

print("\nDivision of Series:")
print(s1 / s2)