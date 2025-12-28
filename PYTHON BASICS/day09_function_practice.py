# Day 9: Function Practice
# Topics:
# logic building using functions

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

def calculate_area(length, breadth):
    return length * breadth

# Function calls
num = int(input("Enter a number: "))
print("Is even:", is_even(num))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Maximum number:", find_max(x, y))

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area of rectangle:", calculate_area(l, b))
