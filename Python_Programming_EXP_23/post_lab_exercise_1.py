import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email_id = input("Enter email ID: ")
if validate_email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
