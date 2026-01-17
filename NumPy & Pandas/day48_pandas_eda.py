"""
Day 48: Exploratory Data Analysis (EDA) with Pandas

Topics covered:
- describe for summaries
- value_counts
- basic insights from data
- identifying patterns

Goal:
Understand data before making assumptions.
"""

import pandas as pd

# Sample dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram", "Sonia"],
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Salary": [70000, 75000, 50000, 52000, 65000, 68000],
    "Experience": [3, 4, 2, 3, 5, 6]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Basic overview
print("\nInfo:")
print(df.info())

print("\nStatistical summary:\n", df.describe())

# Department distribution
print("\nEmployees per department:\n", df["Department"].value_counts())

# Average salary by department
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage salary by department:\n", avg_salary)

# High earners
high_earners = df[df["Salary"] > 65000]
print("\nEmployees earning more than 65000:\n", high_earners)

# Experience vs salary insight
print("\nExperience and Salary:\n", df[["Experience", "Salary"]])

# Key takeaways:
# - Always inspect data before analysis
# - value_counts helps understand categories
# - groupby reveals hidden patterns
