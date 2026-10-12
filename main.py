"""Student Performance Analytics System - main program."""

import numpy as np
import pandas as pd
import functions as fn

pd.set_option("display.width", 150)
pd.set_option("display.max_columns", 20)


def heading(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


def main():
    # ---- Step 2: Read the data ----
    df = fn.load_data("students.csv")
    subjects = fn.get_subject_columns(df)

    heading("1. DATASET OVERVIEW")
    print(f"Number of records : {len(df)}")
    print(f"Columns           : {list(df.columns)}")
    print(f"Subjects          : {subjects}")
    print("\nFirst 5 records:")
    print(df.head())

    # ---- Step 3: Process the data ----
    df = fn.calculate_total_and_average(df, subjects)
    df = fn.add_grades(df)
    df = fn.add_pass_fail(df, subjects)

    heading("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]]
          .to_string(index=False))

    # ---- Step 4: Analysis ----
    heading("3. CLASS PERFORMANCE")
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    print(f"Overall class average : {np.mean(df['Average']):.2f}")
    print(f"Highest average       : {best['Name']} ({best['Average']})")
    print(f"Lowest average        : {worst['Name']} ({worst['Average']})")

    passed = (df["Result"] == "Pass").sum()
    failed = len(df) - passed
    print(f"Passed : {passed}   Failed : {failed}   "
          f"Pass % : {passed / len(df) * 100:.1f}%")

    print("\nGrade distribution:")
    print(df["Grade"].value_counts().sort_index().to_string())

    heading("4. SUBJECT-WISE ANALYSIS")
    subject_df = fn.subject_analysis(df, subjects)
    print(subject_df.to_string(index=False))
    top_subject = subject_df.loc[subject_df["Average"].idxmax()]
    low_subject = subject_df.loc[subject_df["Average"].idxmin()]
    print(f"\nBest subject  : {top_subject['Subject']} ({top_subject['Average']})")
    print(f"Weakest subject: {low_subject['Subject']} ({low_subject['Average']})")

    heading("5. TOP 3 PERFORMERS")
    print(fn.get_top_performers(df, 3)[["Student_ID", "Name", "Department",
                                        "Average", "Grade"]].to_string(index=False))

    heading("6. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df))

    heading("7. STUDENTS NEEDING ATTENTION")
    failing = df[df["Result"] == "Fail"]
    print("Failed students:")
    print(failing[["Name", "Average", "Result"]].to_string(index=False))
    shortage = df[df["Attendance_Status"] == "Shortage"]
    print(f"\nAttendance below {fn.ATTENDANCE_LIMIT}%:")
    print(shortage[["Name", "Attendance"]].to_string(index=False))

    # Save full results
    df.to_csv("results.csv", index=False)
    print("\nFull results saved to results.csv")


if __name__ == "__main__":
    main()