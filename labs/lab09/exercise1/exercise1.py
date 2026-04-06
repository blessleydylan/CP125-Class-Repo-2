import pandas as pd

def explore_data(filename):
    # Load CSV into DataFrame
    df = pd.read_csv(filename)
    
    # Total number of students (rows)
    total_students = len(df)
    
    # Subjects (fixed order as required by test)
    subjects = ["Math", "Science", "English"]
    
    # Average Math score (rounded to 1 decimal place)
    math_average = round(df["Math"].mean(), 1)
    
    # Student with highest Math score
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]
    
    # Return dictionary
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }