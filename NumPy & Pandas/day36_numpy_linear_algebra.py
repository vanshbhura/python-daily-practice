"""
Day 36: NumPy Linear Algebra Basics

Topics covered:
- Dot product
- Matrix multiplication
- Transpose
- Identity matrix

Goal:
Understand how NumPy handles matrix operations.
"""

import numpy as np

# Vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Dot product
dot_product = np.dot(v1, v2)
print("Dot product:", dot_product)

# Matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication
matmul = np.dot(A, B)
print("Matrix multiplication:\n", matmul)

# Using @ operator
matmul_operator = A @ B
print("Matrix multiplication using @:\n", matmul_operator)

# Transpose
print("Transpose of A:\n", A.T)

# Identity matrix
identity = np.eye(3)
print("Identity matrix:\n", identity)

# Key takeaways:
# - Dot product combines vectors into a scalar
# - Matrix multiplication follows strict shape rules
# - Transpose flips rows and columns
# - Identity matrix acts like 1 in multiplication
