# Day 2: Conditional Statements
# Topics:
# if, elif, else, comparison operators

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age == 18:
    print("You just became an adult")
else:
    print("You are an adult")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
