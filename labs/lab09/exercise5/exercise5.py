import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    # Filter students scoring >85 in all subjects
    filtered = df[
        (df["Math"] > 85) &
        (df["Science"] > 85) &
        (df["English"] > 85)
    ]
    
    names = set(filtered["Name"])
    
    return {
        "count": len(names),
        "names": names
    }