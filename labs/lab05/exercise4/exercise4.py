def filter_query_times(query_times):
    if len(query_times) == 0:
        return []

    sorted_times = sorted(query_times)
    n = len(sorted_times)
    
    mean = sum(sorted_times) / n
    variance = (sum(x * x for x in sorted_times) / n) - (mean ** 2)
    std_dev = variance ** 0.5
    
    upper_limit = mean + std_dev

    return [x for x in sorted_times if x <= upper_limit]



# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
