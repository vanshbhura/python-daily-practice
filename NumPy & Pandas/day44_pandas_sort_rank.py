"""
Day 44: Pandas Sorting and Ranking

Topics covered:
- sort_values
- sort_index
- rank
- Ordering data for analysis

Goal:
Arrange data meaningfully for comparison and reporting.
"""

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram"],
    "Total": [233, 253, 277, 183, 258]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Sort by Total marks (descending)
sorted_by_total = df.sort_values(by="Total", ascending=False)
print("\nSorted by Total (descending):\n", sorted_by_total)

# Ranking
df["Rank"] = df["Total"].rank(ascending=False, method="dense")
print("\nWith Rank:\n", df)

# Sort by Rank
ranked_df = df.sort_values(by="Rank")
print("\nSorted by Rank:\n", ranked_df)

# Sort by index
print("\nSorted by index:\n", df.sort_index())

# Key takeaways:
# - sort_values orders data by columns
# - rank assigns relative positions
# - Sorting improves readability and insight
