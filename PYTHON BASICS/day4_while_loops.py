# Day 4: While Loops
# Topics:
# while loop, break, continue

count = 1

print("Counting from 1 to 5 using while loop:")
while count <= 5:
    print(count)
    count += 1

print("\nSkipping number 3 using continue:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

print("\nStopping loop when number reaches 4:")
num = 0
while True:
    num += 1
    if num == 4:
        break
    print(num)
