import pandas as pd
import matplotlib.pyplot as plt

def show_science_distribution(filename):
    df = pd.read_csv(filename)
    
    # Plot histogram
    plt.hist(df["Science"], bins=10)
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")
    plt.show()
    
    return len(df)

show_science_distribution("CP125-Class-Repo-2\labs\lab09\data\students.csv")