
def is_critical_hit(luck):
    """
    Returns True if luck is above 70.
    """
    # TODO: Implement this function
    if luck > 70:
        return True
    else:
        return False

def calculate_raw_damage(base_attack, is_crit):
    """
    Doubles the base attack if it's a critical hit.
    """
    # TODO: Implement this function
    if is_crit:
        base_attack = base_attack *2
    else:
        base_attack = base_attack
    return base_attack

def calculate_final_health(current_health, raw_damage, defense):
    """
    Calculates final health after damage.
    Actual damage = raw_damage - defense.
    Damage cannot be negative.
    Final health cannot go below 0.
    """
    # TODO: Implement this function
    final_health = 0
    if defense >= raw_damage:
        final_health = current_health
    else:
        final_health = current_health - (raw_damage - defense)
    if final_health <= 0:
        final_health = 0
    return final_health

print(calculate_final_health(100, 10, 20))