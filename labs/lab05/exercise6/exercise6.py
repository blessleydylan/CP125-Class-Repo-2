
def find_slow_endpoints(api_calls, threshold):
    # Collect response times for successful (200) calls only
    endpoint_times = {}

    for endpoint, response_time, status in api_calls:
        if status == 200:
            endpoint_times.setdefault(endpoint, []).append(response_time)

    slow_endpoints = []

    for endpoint, times in endpoint_times.items():
        # Must have at least two successful calls
        if len(times) >= 2:
            average_time = sum(times) / len(times)
            # Strictly greater than threshold
            if average_time > threshold:
                slow_endpoints.append(endpoint)

    # Return endpoints sorted alphabetically
    return sorted(slow_endpoints)



api_calls = [
    ("/login", 45, 200), 
    ("/login", 120, 200), 
    ("/data", 80, 200),
    ("/login", 50, 500),
    ("/data", 95, 200), 
    ("/search", 30, 200),
    ("/health", 150, 200)
]

result = find_slow_endpoints(api_calls, 70)
print(f"Slow endpoints: {result}")
