# Day 13: Recursion
# Topics:
# recursive function, base case

# Example 1: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# Example 2: Sum of first n numbers
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

print("Sum of first 5 numbers:", sum_n(5))
