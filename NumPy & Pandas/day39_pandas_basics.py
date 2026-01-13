"""
Day 39: Pandas Basics

Topics covered:
- Pandas Series
- Pandas DataFrame
- Reading basic data
- head, info, describe

Goal:
Understand how Pandas structures tabular data on top of NumPy.
"""

import pandas as pd
import numpy as np

# Creating a Series
scores = pd.Series([78, 85, 92, 60, 88])
print("Series:\n", scores)

# Creating a DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram"],
    "Math": [78, 85, 92, 60, 88],
    "Science": [80, 89, 95, 65, 90],
    "English": [75, 82, 90, 58, 85]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Basic inspection
print("\nFirst 3 rows:\n", df.head(3))
print("\nInfo:")
print(df.info())

print("\nDescribe:\n", df.describe())

# Accessing columns
print("\nMath column:\n", df["Math"])

# Mean using Pandas (built on NumPy)
print("\nAverage Math score:", df["Math"].mean())

# Key takeaways:
# - Series = 1D labeled data
# - DataFrame = 2D labeled data (rows + columns)
# - Pandas uses NumPy under the hood
