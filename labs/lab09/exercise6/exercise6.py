import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    critical = df[
        (df["Current_Stock"] < df["Reorder_Threshold"]) &
        (df["Days_Since_Last_Restock"] > 30)
    ]
    
    products = set(critical["Product_Name"])
    
    return {
        "total_products": len(df),
        "critical_count": len(products),
        "critical_products": products
    }