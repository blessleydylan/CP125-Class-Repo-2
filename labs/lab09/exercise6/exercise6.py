import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    critical = df[
        (df["StockLevel"] < df["ReorderThreshold"]) &
        (df["DaysSinceRestock"] > 30)
    ]
    
    products = set(critical["ProductName"])
    
    return {
        "total_products": len(df),
        "critical_count": len(products),
        "critical_products": products
    }