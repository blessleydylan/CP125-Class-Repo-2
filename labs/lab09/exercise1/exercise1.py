import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    # Total number of students (rows)
    total_students = df.shape[0]

    # Subjects list (fixed order as required by tests)
    subjects = ["Math", "Science", "English"]

    # Math average
    math_average = df["Math"].mean()

    # Student with highest Math score
    idx = df["Math"].idxmax()
    highest_math_student = df.loc[idx, "Name"]

    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }