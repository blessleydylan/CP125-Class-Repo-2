def calculate_xp_required(current_level):
    """
    Calculate XP needed for next level (level * 100).
    """
    # TODO: Implement this
    xp_required = current_level * 100
    return xp_required


def can_level_up(current_xp, required_xp):
    """
    Check if player has enough XP to level up.
    """
    # TODO: Implement this
    if current_xp >= required_xp:
        return True
    else:
        return False


def calculate_final_level(total_xp):
    """
    Calculate the final level reached.
    """
    # TODO: Implement this
    required_xp = 100
    level = 1
    while True:
        if total_xp >= required_xp:
            level += 1
            total_xp -= required_xp
            required_xp += 100
        else:
            break
    return level

def calculate_remaining_xp(total_xp):
    """
    Calculate XP leftover after leveling.
    """
    # TODO: Implement this
    required_xp = 100
    level = 1
    while True:
        if total_xp >= required_xp:
            level += 1
            total_xp -= required_xp
            required_xp += 100
        else:
            break
    return total_xp
