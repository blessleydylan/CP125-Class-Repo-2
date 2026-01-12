def analyze_performance(lap_times):
    first_half = []
    second_half = []
    
    total_laps = len(lap_times)
    midpoint = (total_laps + 1) // 2  
    
    for i in range(total_laps):
        if i < midpoint:
            first_half.append(lap_times[i])
        else:
            second_half.append(lap_times[i])
    first_avg = sum(first_half) / len(first_half)
    second_avg = sum(second_half) / len(second_half)
    return second_avg > first_avg


# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
