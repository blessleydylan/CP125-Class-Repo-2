def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    next_height = 0.8 * current_height
    return next_height


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    if height < 1:
        return True
    else:
        return False


def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    total_bounce = 0
    # TODO: Implement this
    while initial_height >= 1:
        total_bounce += 1
        initial_height = initial_height *0.8
    return total_bounce



def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    distance = 0
    distance += initial_height
    if initial_height == 1:
        initial_height = 0
        distance = 1.8
    while initial_height >= 1:
        initial_height = initial_height * 0.8
        distance += initial_height * 2
    return distance

print(calculate_total_distance(1))