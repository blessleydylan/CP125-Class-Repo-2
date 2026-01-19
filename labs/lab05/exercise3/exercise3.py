def find_bottleneck_index(traceroute):
    max_increase = 0
    bottleneck_index = 0

    for i in range(len(traceroute) - 1):
        _, prev_ms = traceroute[i]
        _, current_ms = traceroute[i + 1]

        increase = current_ms - prev_ms
        if increase > max_increase:
            max_increase = increase
            bottleneck_index = i

    return bottleneck_index

# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
