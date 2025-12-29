# Day 11: List Comprehension
# Topics:
# basic list comprehension with conditions

numbers = [1, 2, 3, 4, 5]

# Normal loop
squares_loop = []
for num in numbers:
    squares_loop.append(num * num)

print("Squares using loop:", squares_loop)

# List comprehension
squares_comp = [num * num for num in numbers]
print("Squares using list comprehension:", squares_comp)

# List comprehension with condition
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
