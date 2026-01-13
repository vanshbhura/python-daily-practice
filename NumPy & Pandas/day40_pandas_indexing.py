"""
Day 40: Pandas Indexing (loc vs iloc)

Topics covered:
- Selecting rows and columns
- loc (label-based indexing)
- iloc (position-based indexing)
- Boolean filtering

Goal:
Access data correctly without confusion or bugs.
"""

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram"],
    "Math": [78, 85, 92, 60, 88],
    "Science": [80, 89, 95, 65, 90],
    "English": [75, 82, 90, 58, 85]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# iloc: position-based indexing
print("\nFirst row using iloc:\n", df.iloc[0])
print("\nFirst two rows using iloc:\n", df.iloc[0:2])
print("\nMath and Science columns using iloc:\n", df.iloc[:, 1:3])

# loc: label-based indexing
print("\nRow with index 2 using loc:\n", df.loc[2])
print("\nSelect specific columns using loc:\n", df.loc[:, ["Math", "English"]])

# Boolean indexing
print("\nStudents with Math > 80:\n", df[df["Math"] > 80])

# Combine conditions
print(
    "\nStudents with Math > 80 and Science > 85:\n",
    df[(df["Math"] > 80) & (df["Science"] > 85)]
)

# Key takeaways:
# - iloc uses integer positions
# - loc uses labels (index/column names)
# - Boolean conditions are very common in real analysis
