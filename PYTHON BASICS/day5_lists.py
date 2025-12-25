# Day 5: Lists
# Topics:
# create list, access elements, update elements

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Updating elements
numbers[2] = 35
print("Updated list:", numbers)

# Adding elements
numbers.append(60)
print("After adding an element:", numbers)

# Removing elements
numbers.remove(20)
print("After removing an element:", numbers)
