import pandas as pd

def compare_averages(filename):
    # Load CSV
    df = pd.read_csv(filename)
    
    # Calculate averages (rounded to 1 decimal)
    math_avg = round(df["Math"].mean(), 1)
    science_avg = round(df["Science"].mean(), 1)
    english_avg = round(df["English"].mean(), 1)
    
    # Store in dictionary for easy comparison
    averages = {
        "Math": math_avg,
        "Science": science_avg,
        "English": english_avg
    }
    
    # Identify best and worst subjects
    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)
    
    # Return final dictionary
    return {
        "Math": math_avg,
        "Science": science_avg,
        "English": english_avg,
        "best_subject": best_subject,
        "worst_subject": worst_subject
    }