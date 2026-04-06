import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    total_students = len(df)
    
    subjects = ["Math", "Science", "English"]
    
    math_average = round(df["Math"].mean(), 1)
    
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]
    
    # Return dictionary
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }