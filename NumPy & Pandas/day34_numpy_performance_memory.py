"""
Day 34: NumPy Performance and Memory Behavior

Topics covered:
- Loop vs vectorized performance
- Copy vs view in NumPy
- How memory sharing affects data

Goal:
Write fast NumPy code without unintended side effects.
"""

import numpy as np
import time

# Large array for performance testing
large_array = np.arange(5_000_000)

# Loop-based computation
start = time.time()
loop_result = []
for x in large_array:
    loop_result.append(x * 2)
end = time.time()
print("Loop time:", end - start)

# Vectorized computation
start = time.time()
vector_result = large_array * 2
end = time.time()
print("Vectorized time:", end - start)

# Copy vs view demonstration
original = np.array([10, 20, 30, 40, 50])
view_slice = original[1:4]
copy_slice = original[1:4].copy()

view_slice[0] = 999
copy_slice[1] = 555

print("Original array after view modification:", original)
print("View slice:", view_slice)
print("Copy slice:", copy_slice)

# Memory sharing check
print("View shares memory:", np.shares_memory(original, view_slice))
print("Copy shares memory:", np.shares_memory(original, copy_slice))

# Key takeaways:
# - Vectorized operations are significantly faster
# - Slices usually return views, not copies
# - Always use .copy() when data independence is required
