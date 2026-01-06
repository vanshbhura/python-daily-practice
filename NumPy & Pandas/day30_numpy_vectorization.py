"""
Day 30: NumPy Vectorized Operations and Broadcasting

Topics covered:
- Element-wise operations
- Vectorization vs loops
- Broadcasting rules

Goal:
Understand why NumPy is fast and how to use it correctly.
"""

import numpy as np
import time

# Sample arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Element-wise operations
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# Broadcasting with scalar
print("Add scalar:", a + 5)
print("Multiply by scalar:", a * 3)

# Broadcasting with 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix + 10:\n", matrix + 10)

# Broadcasting between arrays
row = np.array([1, 2, 3])
print("Matrix + row:\n", matrix + row)

# Loop vs vectorized performance
large_array = np.arange(1_000_000)

# Loop approach
start = time.time()
result_loop = []
for x in large_array:
    result_loop.append(x * 2)
end = time.time()
print("Loop time:", end - start)

# Vectorized approach
start = time.time()
result_vectorized = large_array * 2
end = time.time()
print("Vectorized time:", end - start)

# Key takeaways:
# - Vectorized operations avoid Python loops
# - Broadcasting lets NumPy operate on different shapes
# - Vectorization is faster and cleaner
