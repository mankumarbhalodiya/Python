number = int(input("Enter a number: "))
n = abs(number)
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print("Product of digits:", product)