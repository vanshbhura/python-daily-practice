# Day 15: Exception Handling
# Topics:
# try, except, else, finally

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Calculation successful.")

finally:
    print("Program execution completed.")
