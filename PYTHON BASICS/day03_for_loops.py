# easy
# Day 3: For Loops
# Topics:
# for loop, range(), repetition

print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nEven numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("\nMultiplication table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
