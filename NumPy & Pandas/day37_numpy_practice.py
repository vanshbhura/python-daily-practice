"""
Day 37: NumPy Mini Practice

Topics:
- Array creation
- Indexing and slicing
- Vectorized operations
- Aggregations
- Sorting and filtering

Goal:
Apply NumPy concepts without introducing anything new.
"""

import numpy as np

# Create a dataset (marks of 5 students in 4 subjects)
marks = np.array([
    [78, 85, 90, 88],
    [65, 70, 72, 68],
    [92, 95, 94, 96],
    [55, 60, 58, 62],
    [80, 82, 85, 83]
])

print("Marks:\n", marks)

# 1. Total marks per student
student_totals = marks.sum(axis=1)
print("Total marks per student:", student_totals)

# 2. Average marks per subject
subject_averages = marks.mean(axis=0)
print("Average marks per subject:", subject_averages)

# 3. Highest scorer (student index)
top_student_index = np.argmax(student_totals)
print("Top student index:", top_student_index)

# 4. Students who passed all subjects (>=60)
passed_all = np.all(marks >= 60, axis=1)
print("Passed all subjects:", passed_all)

# 5. Marks greater than 90
high_scores = marks[marks > 90]
print("Marks greater than 90:", high_scores)

# 6. Sort students by total marks
sorted_indices = np.argsort(student_totals)[::-1]
sorted_marks = marks[sorted_indices]
print("Students sorted by total marks:\n", sorted_marks)

# Key takeaways:
# - axis helps control direction of aggregation
# - Boolean conditions can filter multidimensional data
# - argsort is useful for ranking
