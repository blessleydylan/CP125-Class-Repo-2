
def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    # TODO: Implement this function
    battery_used = 0
    while distance >= 10:
        battery_used += 1.5
        distance -= 10
    return battery_used

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    # TODO: Implement this function
    if is_sport_mode == True:
        usage = usage * 1.5
    else:
        usage = usage
    return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    # TODO: Implement this function
    usage = apply_mode_bonus(calculate_base_usage(distance * 2), is_sport_mode)
    if current_battery >= usage:
        return True
    else:
        return False

print(has_enough_battery(100, 44, True))