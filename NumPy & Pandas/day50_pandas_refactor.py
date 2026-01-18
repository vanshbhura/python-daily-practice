"""
Day 50: Refactoring Pandas Mini Project

Goal:
- Improve readability
- Use functions
- Reduce repetition
- Make code easier to maintain
"""

import pandas as pd


def load_data():
    """Create and return the student dataset."""
    data = {
        "Name": ["Aman", "Riya", "Karan", "Neha", "Vikram", "Sonia"],
        "Maths": [78, 85, 92, 60, 88, 95],
        "Science": [80, 89, 95, 65, 90, 93],
        "English": [75, 82, 90, 58, 85, 91]
    }
    return pd.DataFrame(data)


def assign_grade(avg):
    """Return grade based on average marks."""
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def process_data(df):
    """Add Total, Average, and Grade columns."""
    subjects = ["Maths", "Science", "English"]
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = (df["Total"] / len(subjects)).round(2)
    df["Grade"] = df["Average"].apply(assign_grade)
    return df


def main():
    df = load_data()
    print("Original Data:\n", df)

    df = process_data(df)
    print("\nProcessed Data:\n", df)

    topper = df.loc[df["Total"].idxmax()]
    print("\nTop Performer:\n", topper)

    subject_avg = df[["Maths", "Science", "English"]].mean()
    print("\nSubject-wise Averages:\n", subject_avg)

    failed = df[(df[["Maths", "Science", "English"]] < 60).any(axis=1)]
    print("\nStudents who failed:\n", failed)


if __name__ == "__main__":
    main()

# Key takeaways:
# - Functions make code readable and reusable
# - Refactoring improves clarity without changing behavior
# - Clean code scales better than clever code
