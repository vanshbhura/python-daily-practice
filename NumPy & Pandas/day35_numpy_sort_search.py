"""
Day 35: NumPy Sorting, Searching, and Conditional Selection

Topics covered:
- sort and argsort
- where for conditional selection
- min/max index finding

Goal:
Select and reorder data without manual loops.
"""

import numpy as np

# Sample data
data = np.array([45, 12, 78, 34, 89, 21])
print("Original data:", data)

# Sorting
sorted_data = np.sort(data)
print("Sorted data:", sorted_data)

# Argsort (indices that would sort the array)
sorted_indices = np.argsort(data)
print("Indices that sort the array:", sorted_indices)
print("Data sorted using argsort:", data[sorted_indices])

# Finding indices of min and max
min_index = np.argmin(data)
max_index = np.argmax(data)
print("Index of minimum value:", min_index)
print("Index of maximum value:", max_index)

# Conditional selection using where
high_values = np.where(data > 50, data, -1)
print("Values > 50 (else -1):", high_values)

# Filtering using boolean indexing
filtered = data[data > 50]
print("Filtered values (>50):", filtered)

# Practical example: grading logic
marks = np.array([35, 67, 82, 49, 90])

results = np.where(marks >= 40, "Pass", "Fail")
print("Results:", results)

# Key takeaways:
# - sort returns a new sorted array
# - argsort is useful when order matters
# - where replaces many conditional loops
