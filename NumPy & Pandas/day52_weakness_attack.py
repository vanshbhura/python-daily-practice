"""
Day 52: Weakness Attack – Axis and GroupBy Reinforcement

Focus:
- axis understanding
- groupby mental model
- avoiding silent logic bugs

Goal:
Turn a weak topic into a reliable one.
"""

import pandas as pd
import numpy as np

# Create dataset
data = {
    "Team": ["A", "A", "B", "B", "C", "C"],
    "Player": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "Score": [10, 20, 15, 25, 30, 35]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Axis recap with NumPy-style thinking
scores_matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nScores matrix:\n", scores_matrix)
print("Sum axis=0 (column-wise):", scores_matrix.sum(axis=0))
print("Sum axis=1 (row-wise):", scores_matrix.sum(axis=1))

# GroupBy recap
grouped = df.groupby("Team")["Score"]

print("\nAverage score per team:\n", grouped.mean())
print("\nTotal score per team:\n", grouped.sum())

# Combining conditions
high_scorers = df[df["Score"] > 20]
print("\nPlayers with score > 20:\n", high_scorers)

# Mental model check
# axis=0 -> collapse rows
# axis=1 -> collapse columns
# groupby = split -> apply -> combine
