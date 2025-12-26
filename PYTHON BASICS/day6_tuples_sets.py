# Day 6: Tuples and Sets
# Topics:
# tuple, set, basic operations

# Tuple example (immutable)
fruits_tuple = ("apple", "banana", "cherry")
print("Tuple:", fruits_tuple)

print("First fruit:", fruits_tuple[0])
print("Length of tuple:", len(fruits_tuple))

# Set example (unique values, unordered)
numbers_set = {1, 2, 3, 3, 4, 5}
print("Set:", numbers_set)

# Adding element to set
numbers_set.add(6)
print("Set after adding 6:", numbers_set)

# Removing element from set
numbers_set.remove(2)
print("Set after removing 2:", numbers_set)

# Difference demonstration
fruits_list = ["apple", "banana", "cherry", "apple"]
print("\nList allows duplicates:", fruits_list)
print("Set removes duplicates:", set(fruits_list))
