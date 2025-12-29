# Day 12: Basic Problem Solving
# Using loops, conditions, lists, and functions

# Problem 1: Count even and odd numbers in a list
numbers = [10, 15, 20, 25, 30]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)


# Problem 2: Find sum of elements in a list
total = 0
for num in numbers:
    total += num

print("Sum of numbers:", total)


# Problem 3: Check if a number exists in a list
search = int(input("Enter number to search: "))

if search in numbers:
    print(search, "is present in the list")
else:
    print(search, "is not present in the list")
