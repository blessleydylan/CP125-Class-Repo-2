import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)
    
    # Average performance
    avg_performance = round(df["Performance"].mean(), 1)
    
    # Minimum years required
    min_years = 2
    
    # Filter candidates
    filtered = df[
        (df["Performance"] > avg_performance) &
        (df["Years"] >= min_years)
    ]
    
    names = set(filtered["Name"])
    
    return {
        "average_performance": avg_performance,
        "min_years_required": min_years,
        "candidate_count": len(names),
        "candidate_names": names
    }