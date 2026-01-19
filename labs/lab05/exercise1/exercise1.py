
def was_backward_detected(waypoints):
    for i in range(1, len(waypoints)):
        prev_x, prev_y, _ = waypoints[i - 1]
        curr_x, curr_y, _ = waypoints[i]

        if curr_x < prev_x or curr_y < prev_y:
            return True

    return False


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
