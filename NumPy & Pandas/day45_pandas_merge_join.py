"""
Day 45: Pandas Merging and Joining

Topics covered:
- merge (inner, left, right)
- concat
- Combining multiple DataFrames

Goal:
Combine related datasets correctly without losing or duplicating data.
"""

import pandas as pd

# Student details
students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Neha"]
})

# Marks data
marks = pd.DataFrame({
    "StudentID": [1, 2, 3, 5],
    "Math": [78, 85, 92, 60]
})

print("Students:\n", students)
print("\nMarks:\n", marks)

# Inner join
inner_merge = pd.merge(students, marks, on="StudentID", how="inner")
print("\nInner merge:\n", inner_merge)

# Left join
left_merge = pd.merge(students, marks, on="StudentID", how="left")
print("\nLeft merge:\n", left_merge)

# Right join
right_merge = pd.merge(students, marks, on="StudentID", how="right")
print("\nRight merge:\n", right_merge)

# Concatenation
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

concat_df = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame:\n", concat_df)

# Key takeaways:
# - merge combines DataFrames using keys
# - join type controls which rows are kept
# - concat stacks DataFrames along an axis
