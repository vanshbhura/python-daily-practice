"""
Day 49: Pandas Mini Project – Student Performance Analysis

Dataset:
- Student marks across subjects

Tasks:
- Load data
- Clean data
- Analyze performance
- Generate insights

Goal:
Apply Pandas concepts end-to-end on one dataset.
"""

import pandas as pd

# Create dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram", "Sonia"],
    "Maths": [78, 85, 92, 60, 88, 95],
    "Science": [80, 89, 95, 65, 90, 93],
    "English": [75, 82, 90, 58, 85, 91]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Total and average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = (df["Total"] / 3).round(2)

# Grade assignment
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print("\nWith Total, Average, and Grade:\n", df)

# Top performer
topper = df.loc[df["Total"].idxmax()]
print("\nTop Performer:\n", topper)

# Subject-wise averages
subject_avg = df[["Maths", "Science", "English"]].mean()
print("\nSubject-wise Average Marks:\n", subject_avg)

# Students who failed (any subject < 60)
failed_students = df[(df[["Maths", "Science", "English"]] < 60).any(axis=1)]
print("\nStudents who failed at least one subject:\n", failed_students)

# Key takeaways:
# - Combined multiple Pandas operations
# - Avoided loops using vectorized logic
# - Extracted meaningful insights from data
