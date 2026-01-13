"""
Day 41: Pandas Data Cleaning

Topics covered:
- Handling missing values
- dropna and fillna
- Data type conversion
- Renaming columns

Goal:
Clean messy data instead of pretending it is perfect.
"""

import pandas as pd
import numpy as np

# Create messy DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram"],
    "Math": [78, None, 92, 60, None],
    "Science": [80, 89, None, 65, 90],
    "English": ["75", "82", "90", None]()
