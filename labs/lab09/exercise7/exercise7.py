import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)

    avg_performance = round(df["PerformanceScore"].mean(), 1)
    
    min_years = 2
    
    filtered = df[
        (df["PerformanceScore"] > avg_performance) &
        (df["Years"] >= min_years)
    ]
    
    names = set(filtered["Name"])
    
    return {
        "average_performance": avg_performance,
        "min_years_required": min_years,
        "candidate_count": len(names),
        "candidate_names": names
    }