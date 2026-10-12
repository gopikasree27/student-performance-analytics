# 1. Project Title
**Student Performance Analytics System**
Name: Gopikasree M | Batch: Python with AI, EWB Courses | Roll/ID: STU68202a527d9531746938450

# 2. Objective
Teachers often have raw marks but no quick summary. This project reads student
records and automatically calculates totals, averages, grades, pass/fail status,
subject-wise performance and top performers, so class performance can be
understood at a glance.

# 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (DataFrame loading, grouping, sorting, filtering)

# 4. Dataset Description
`students.csv` has **20 records** with the columns: Student_ID, Name, Department,
Maths, Physics, Chemistry, English, Computer_Science, Attendance.

# 5. Implementation
1. **Load data:** `load_data()` reads the CSV into a Pandas DataFrame.
2. **Inspect:** record count, columns and first rows are printed.
3. **Totals & averages:** `calculate_total_and_average()` converts the marks to a
   NumPy array and uses `np.sum` / `np.mean` with `axis=1` (row-wise).
4. **Grades:** `assign_grade()` applies the grading rule below; `add_grades()` loops over every student.
5. **Pass/Fail:** a student passes only if every subject mark is >= 40 (`add_pass_fail()`).
   Attendance below 75% is flagged as "Shortage".
6. **Subject analysis:** `subject_analysis()` loops over subjects and finds average, highest, lowest and pass count with NumPy.
7. **Top performers:** `get_top_performers()` sorts by average.
8. **Department analysis:** `groupby("Department")` summary.

**Grading rule (based on average):**
A+ >= 90 | A >= 80 | B+ >= 70 | B >= 60 | C >= 50 | D >= 40 | F < 40

# 6. Key Features
- `load_data`, `get_subject_columns`, `calculate_total_and_average`
- `assign_grade`, `add_grades`, `add_pass_fail`
- `subject_analysis`, `get_top_performers`, `department_analysis`
- Results exported to `results.csv`

# 7. Output / Screenshots
Run `python main.py` and add screenshots of the output here:
`![Output](screenshots/output1.png)`

# 8. Final Outcome
The program produces a clear report: class average 70.73, 18 of 20 students
passed, Computer Science is the strongest subject, and the top performer is
Nisha Fathima (93.2 average).

# 9. Challenges & Learning

**Challenges faced and how I solved them**

1. **Opening the correct project folder:** At first VS Code was opened in the
   wrong folder, so the Python interpreter option did not appear and my other
   files were mixed with the project. I solved it by using File -> Open Folder
   and selecting only the `student-performance-analytics` folder.

2. **Terminal in the wrong location:** The terminal was in the `Documents`
   folder, so the program could not find `main.py` and `students.csv`. I fixed
   it by checking that the terminal path ended with the project folder name
   before running `python main.py`.

3. **Installing the libraries:** NumPy and Pandas had to be installed before the
   program could run. I installed them with `pip install numpy pandas`.

4. **Understanding NumPy row-wise calculation:** I was confused about how to
   calculate the total and average for each student. I learned that
   `axis=1` works across each row (one student), while `axis=0` works down each
   column (one subject).

5. **Deciding the pass/fail rule:** I had to decide a clear condition. I chose
   that a student passes only if the marks in every subject are 40 or above.
   This is why a student can have an average above 40 and still fail.

**What I learned**

- How to load a CSV file into a Pandas DataFrame and inspect it.
- How to use NumPy functions (`sum`, `mean`, `max`, `min`) for calculations.
- How to write reusable functions and call them from `main.py`.
- How to use loops and if/elif conditions to assign grades and results.
- How to use Pandas `sort_values`, `groupby` and filtering to find top
  performers, department summaries and failed students.
- How to organise a project into separate files and run it from the terminal.
- How to keep the project in its own folder so it can be uploaded to GitHub.

# 10. GitHub Repository
< https://github.com/gopikasree27/student-performance-analytics>

---
### How to run
pip install numpy pandas
python main.py
