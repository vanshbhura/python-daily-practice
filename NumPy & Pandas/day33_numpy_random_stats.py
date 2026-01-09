"""
Day 33: NumPy Random Numbers and Basic Statistics

Topics covered:
- Random number generation
- Setting random seed
- Basic statistical functions

Goal:
Generate reproducible data and analyze it correctly.
"""

import numpy as np

# Random seed for reproducibility
np.random.seed(42)

# Random numbers
random_ints = np.random.randint(1, 100, size=10)
random_floats = np.random.rand(5)

print("Random integers:", random_ints)
print("Random floats:", random_floats)

# Random normal distribution
normal_data = np.random.randn(1000)
print("Normal distribution sample (first 10):", normal_data[:10])

# Basic statistics
print("Mean:", np.mean(normal_data))
print("Standard deviation:", np.std(normal_data))
print("Minimum:", np.min(normal_data))
print("Maximum:", np.max(normal_data))

# Percentiles
print("25th percentile:", np.percentile(normal_data, 25))
print("50th percentile (median):", np.percentile(normal_data, 50))
print("75th percentile:", np.percentile(normal_data, 75))

# Key takeaways:
# - Setting a seed makes results reproducible
# - rand() generates uniform distribution
# - randn() generates normal distribution
# - Basic stats describe data behavior
