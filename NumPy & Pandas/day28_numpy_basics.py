"""
Day 28: NumPy Basics

Topics covered:
- Introduction to NumPy
- NumPy arrays vs Python lists
- Array creation
- shape and dtype

Goal:
Start thinking in arrays instead of Python lists.
"""

import numpy as np

# Creating NumPy arrays
one_d = np.array([1, 2, 3, 4])
two_d = np.array([[1, 2], [3, 4]])

print("1D array:", one_d)
print("2D array:\n", two_d)

# Shape and data type
print("Shape of 1D array:", one_d.shape)
print("Shape of 2D array:", two_d.shape)

print("Data type of 1D array:", one_d.dtype)
print("Data type of 2D array:", two_d.dtype)

# Array creation functions
zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)

print("Zeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Range array:", range_arr)

# Type conversion
int_array = np.array([1, 2, 3])
float_array = int_array.astype(float)

print("Converted array:", float_array)
print("Converted dtype:", float_array.dtype)

# List vs NumPy array behavior
py_list = [1, 2, 3]
np_array = np.array([1, 2, 3])

print("Python list * 2:", py_list * 2)
print("NumPy array * 2:", np_array * 2)

# Key takeaways:
# - Python lists repeat elements
# - NumPy arrays perform element-wise operations
# - shape describes structure, dtype describes memory type
