"""
Day 29: NumPy Indexing and Slicing

Topics covered:
- Indexing 1D and 2D arrays
- Slicing ranges
- Boolean indexing
- Difference between slicing and copying

Goal:
Access and filter data correctly without corrupting it.
"""

import numpy as np

# Create sample arrays
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("1D array:", arr_1d)
print("2D array:\n", arr_2d)

# Indexing
print("First element of 1D array:", arr_1d[0])
print("Element at row 2, column 3:", arr_2d[1, 2])

# Slicing
print("Slice of 1D array (index 1 to 3):", arr_1d[1:4])
print("First two rows of 2D array:\n", arr_2d[:2])

# Column slicing
print("Second column of 2D array:", arr_2d[:, 1])

# Boolean indexing
mask = arr_1d > 25
print("Boolean mask:", mask)
print("Elements greater than 25:", arr_1d[mask])

# View vs Copy
slice_view = arr_1d[1:4]
slice_view[0] = 999

print("Modified slice:", slice_view)
print("Original array after slice modification:", arr_1d)

# Copy to avoid modifying original
safe_copy = arr_1d[1:4].copy()
safe_copy[0] = 555

print("Safe copy:", safe_copy)
print("Original array remains unchanged:", arr_1d)

# Key takeaways:
# - Slicing returns a view, not a copy
# - Boolean indexing is powerful for filtering
# - Use .copy() when you need independent data
