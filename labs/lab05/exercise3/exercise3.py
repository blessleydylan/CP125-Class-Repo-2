def find_bottleneck_index(traceroute):
    bottleneck = 0
    for i in range (len(traceroute)):
        prev_hop, prev_ms = traceroute[i]
        current_hop, current_ms = traceroute[i + 1]
        if current_hop - prev_ms > bottleneck:
            bottleneck = current_hop - prev_ms
    return bottleneck



# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
