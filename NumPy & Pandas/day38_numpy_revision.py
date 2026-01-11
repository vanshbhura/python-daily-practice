"""
Day 38: NumPy Revision and Cleanup

Goal:
- Revisit important NumPy concepts
- Rewrite small snippets cleanly
- Strengthen mental models (shape, axis, views)

No new concepts introduced.
"""

import numpy as np

# Recreate a sample dataset
data = np.array([
    [12, 15, 18],
    [20, 22, 25],
    [30, 28, 27]
])

print("Data:\n", data)

# Shape and dtype
print("Shape:", data.shape)
print("Dtype:", data.dtype)

# Aggregations
print("Row-wise sum:", data.sum(axis=1))
print("Column-wise mean:", data.mean(axis=0))

# Boolean filtering
above_20 = data[data > 20]
print("Values above 20:", above_20)

# Reshaping
reshaped = data.reshape(1, 9)
print("Reshaped data:", reshaped)

# Copy vs view check
slice_view = data[:, 1]
slice_copy = data[:, 1].copy()

slice_view[0] = 999

print("Data after modifying view:\n", data)
print("Slice copy (safe):", slice_copy)

# Key takeaways:
# - Always track shape before and after operations
# - axis defines direction of aggregation
# - Slices can modify original data unless copied

