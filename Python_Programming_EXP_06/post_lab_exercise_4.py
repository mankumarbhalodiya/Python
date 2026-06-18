num = int(input("Enter a number: "))
num = abs(num)
last_digit = num % 10
while num >= 10:
    num //= 10
first_digit = num
print("First digit:", first_digit)
print("Last digit:", last_digit)