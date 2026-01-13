"""
Day 42: Pandas Column Operations

Topics covered:
- Creating new columns
- Updating existing columns
- apply with lambda functions

Goal:
Transform data using clear, readable logic.
"""

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram"],
    "Maths": [78, 82, 92, 60, 88],
    "Science": [80, 89, 95, 65, 90],
    "English": [75, 82, 90, 58, 85]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Create total marks column
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Create average marks column
df["Average"] = df["Total"] / 3

print("\nWith Total and Average:\n", df)

# Update column values
df["Average"] = df["Average"].round(2)

# Create grade column using apply
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

print("\nWith Grades:\n", df)

# Key takeaways:
# - New columns can be derived from existing ones
# - apply helps run logic row-wise
# - Clear column names improve readability
