n = int(input("Enter a positive number: "))
if n > 0:
    total = n * (n + 1) // 2
    print("Sum =", total)
else:
    print("Please enter a number greater than 0.")