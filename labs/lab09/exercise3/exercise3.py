import pandas as pd
import matplotlib.pyplot as plt

def show_math_trend(filename):
    df = pd.read_csv(filename)
    
    # Plot line chart
    plt.plot(df.index, df["Math"])
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")
    plt.show()
    
    return len(df)