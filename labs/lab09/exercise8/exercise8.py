import pandas as pd
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    df = pd.read_csv(filename)
    
    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]
    max_scores = [df[sub].max() for sub in subjects]
    
    plt.plot(subjects, max_scores, marker='o')
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()
    
    return len(df)

plot_subject_maximums("CP125-Class-Repo-2\labs\lab09\data\students.csv")