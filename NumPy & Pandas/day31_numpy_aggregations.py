"""
Day 31: NumPy Aggregations and Axis

Topics covered:
- sum, mean, min, max
- Understanding axis in NumPy
- Row-wise vs column-wise operations

Goal:
Remove confusion around axis and aggregated operations.
"""

import numpy as np

# Sample 2D array
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Data:\n", data)

# Basic aggregations
print("Total sum:", data.sum())
print("Mean:", data.mean())
print("Minimum:", data.min())
print("Maximum:", data.max())

# Axis explanation
print("Sum along axis=0 (column-wise):", data.sum(axis=0))
print("Sum along axis=1 (row-wise):", data.sum(axis=1))

print("Mean along axis=0:", data.mean(axis=0))
print("Mean along axis=1:", data.mean(axis=1))

# Practical example
# Total marks of each student (rows = students)
student_totals = data.sum(axis=1)
print("Student totals:", student_totals)

# Average marks per subject (columns = subjects)
subject_averages = data.mean(axis=0)
print("Subject averages:", subject_averages)

# Key takeaways:
# - axis=0 collapses rows (operates down columns)
# - axis=1 collapses columns (operates across r
