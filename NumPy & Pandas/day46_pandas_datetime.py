"""
Day 46: Pandas Date and Time Handling

Topics covered:
- to_datetime
- DatetimeIndex
- Extracting date components
- Time-based filtering

Goal:
Work confidently with time-based data.
"""

import pandas as pd

# Create DataFrame with date strings
data = {
    "Date": [
        "2024-01-01",
        "2024-01-05",
        "2024-01-10",
        "2024-02-01",
        "2024-02-15"
    ],
    "Sales": [200, 450, 300, 500, 700]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"])
print("\nWith datetime conversion:\n", df)

# Set Date as index
df.set_index("Date", inplace=True)
print("\nDate as index:\n", df)

# Extract date components
df["Month"] = df.index.month
df["Year"] = df.index.year
print("\nWith Month and Year:\n", df)

# Time-based filtering
jan_sales = df["2024-01"]
print("\nJanuary sales:\n", jan_sales)

# Resampling (monthly sum)
monthly_sales = df.resample("M").sum()
print("\nMonthly sales:\n", monthly_sales)

# Key takeaways:
# - Always convert strings to datetime
# - DatetimeIndex enables powerful time slicing
# - Resample is essential for time-series analysis
