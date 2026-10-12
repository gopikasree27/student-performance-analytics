"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

# ---- Rules (change these in one place) ----
PASS_MARK = 40            # minimum marks needed in EVERY subject to pass
ATTENDANCE_LIMIT = 75     # attendance below this % is flagged as shortage


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def get_subject_columns(df):
    """Subject columns = every column except the student detail columns."""
    non_subjects = ["Student_ID", "Name", "Department", "Attendance"]
    return [col for col in df.columns if col not in non_subjects]


def calculate_total_and_average(df, subjects):
    """Add Total and Average columns using NumPy."""
    marks = df[subjects].to_numpy()               # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)           # row-wise sum
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average):
    """Grading rule based on a student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def add_grades(df):
    """Loop through every student's average and assign a grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def add_pass_fail(df, subjects):
    """Pass only if the student scored >= PASS_MARK in every subject."""
    results = []
    for _, row in df.iterrows():
        if (row[subjects] >= PASS_MARK).all():
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= ATTENDANCE_LIMIT, "OK", "Shortage"
    )
    return df


def subject_analysis(df, subjects):
    """Average, highest, lowest and pass count for every subject."""
    rows = []
    for subject in subjects:
        scores = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(scores)), 2),
            "Highest": int(np.max(scores)),
            "Lowest": int(np.min(scores)),
            "Passed": int(np.sum(scores >= PASS_MARK)),
        })
    return pd.DataFrame(rows)


def get_top_performers(df, n=3):
    """Top n students ranked by average marks."""
    return df.sort_values("Average", ascending=False).head(n)


def department_analysis(df):
    """Average marks and pass count per department."""
    return df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)