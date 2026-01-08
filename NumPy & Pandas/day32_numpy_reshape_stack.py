"""
Day 32: NumPy Reshaping, Flattening, and Stacking

Topics covered:
- reshape
- flatten vs ravel
- hstack, vstack, concatenate

Goal:
Understand how to change array structure safely.
"""

import numpy as np

# Base array
arr = np.arange(1, 13)
print("Original array:", arr)
print("Original shape:", arr.shape)

# Reshape
reshaped = arr.reshape(3, 4)
print("Reshaped (3x4):\n", reshaped)

# Flatten vs ravel
flattened = reshaped.flatten()
raveled = reshaped.ravel()

print("Flattened array:", flattened)
print("Raveled array:", raveled)

# Modify raveled array to show view behavior
raveled[0] = 999
print("Modified raveled array:", raveled)
print("Original reshaped array after ravel modification:\n", reshaped)

# Stacking arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Horizontal stack:", np.hstack((a, b)))
print("Vertical stack:\n", np.vstack((a, b)))

# Concatenate
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])

print("Concatenate axis=0:\n", np.concatenate((c, d), axis=0))
print("Concatenate axis=1:\n", np.concatenate((c, d), axis=1))

# Key takeaways:
# - reshape does not change data, only structure
# - flatten creates a copy, ravel returns a view when possible
# - stacking combines arrays along a specified axis
