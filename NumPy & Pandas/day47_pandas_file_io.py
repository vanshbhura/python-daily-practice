"""
Day 47: Pandas File Input and Output

Topics covered:
- Reading CSV files
- Writing CSV files
- Reading and writing JSON
- Basic file inspection

Goal:
Persist data instead of recalculating it every time.
"""

import pandas as pd

# Create sample DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha"],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Write to CSV
df.to_csv("scores.csv", index=False)
print("\nData written to scores.csv")

# Read from CSV
df_csv = pd.read_csv("scores.csv")
print("\nData read from CSV:\n", df_csv)

# Write to JSON
df.to_json("scores.json", orient="records", indent=2)
print("\nData written to scores.json")

# Read from JSON
df_json = pd.read_json("scores.json")
print("\nData read from JSON:\n", df_json)

# Key takeaways:
# - CSV is common and human-readable
# - JSON is structured and flexible
# - index=False avoids junk columns
