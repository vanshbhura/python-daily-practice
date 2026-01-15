"""
Day 43: Pandas GroupBy

Topics covered:
- groupby basics
- Aggregations on groups
- Multiple aggregations

Goal:
Summarize data by categories without manual loops.
"""

import pandas as pd

# Create dataset
data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employee": ["Aman", "Riya", "Karan", "Neha", "Vikram", "Sonia"],
    "Salary": [70000, 75000, 50000, 52000, 65000, 68000]
}

df = pd.DataFrame(data)
print("Employee Data:\n", df)

# Group by Department
grouped = df.groupby("Department")

# Aggregate salary
print("\nAverage salary by department:\n", grouped["Salary"].mean())
print("\nTotal salary by department:\n", grouped["Salary"].sum())
print("\nMax salary by department:\n", grouped["Salary"].max())

# Multiple aggregations
summary = grouped["Salary"].agg(["mean", "min", "max", "count"])
print("\nSalary summary by department:\n", summary)

# Reset index for clean DataFrame
summary_reset = summary.reset_index()
print("\nSummary with reset index:\n", summary_reset)

# Key takeaways:
# - groupby splits data by category
# - Aggregations summarize each group
# - reset_index makes grouped data easier to use
