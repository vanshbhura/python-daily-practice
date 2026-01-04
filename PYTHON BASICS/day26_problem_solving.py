# Day 26: Problem Solving Practice
# Topics:
# loops, conditions, lists, strings

# Problem 1: Reverse a number
num = int(input("Enter a number to reverse: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)


# Problem 2: Count vowels in a string
text = input("\nEnter a string: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


# Problem 3: Find largest element in a list
numbers = [12, 45, 2, 19, 8]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# Problem 4: Check if a number is prime
n = int(input("\nEnter a number to check prime: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
