string = input("enter the string:")
print(string)
reversed = string[::-1]
print("Reversed string:", reversed)
print("original string is:", string)
print("reversed string is:", reversed)
if string == reversed:
    print("string is palindrome")
else:
    print("string is not palindrome")