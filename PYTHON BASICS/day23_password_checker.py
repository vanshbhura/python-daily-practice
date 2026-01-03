# Day 23: Password Strength Checker
# Topics:
# strings, conditions, loops

password = input("Enter your password: ")

has_upper = False
has_digit = False

if len(password) < 8:
    print("Weak password: Must be at least 8 characters")
else:
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_digit:
        print("Strong password")
    else:
        print("Weak password: Must contain at least one uppercase letter and one digit")
