
def is_safe_time(hour, temperature):
    """
    Returns False if 10 <= hour <= 16 (10 AM to 4 PM),
    UNLESS temperature > 40.
    """
    # TODO: Implement this function
    if 10 <= hour <= 16 and temperature <= 40:
        return False
    else:
        return True

def needs_moisture(moisture_level):
    """
    Returns True if moisture < 30.
    """
    # TODO: Implement this function
    if moisture_level< 30:
        return True
    else:
        return False

def should_trigger_pump(moisture, hour, temp):
    """
    Returns True if it needs moisture AND is a safe time.
    """
    # TODO: Implement this function
    if needs_moisture(moisture) and is_safe_time(hour, temp):
        return True
    else:
        return False
