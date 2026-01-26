
def find_conflicting_ports(rules):
    # Track the first action seen for each port
    first_action = {}
    conflicts = {}

    for rule_id, port, action in rules:
        if port not in first_action:
            first_action[port] = action
        else:
            # Conflict occurs when a different action appears
            if first_action[port] != action and port not in conflicts:
                conflicts[port] = rule_id

    # Return sorted list of (port, rule_id)
    return sorted(conflicts.items())



rules = [
    (1, 80, "ALLOW"), 
    (2, 443, "ALLOW"), 
    (3, 80, "BLOCK"),
    (4, 22, "BLOCK"), 
    (5, 443, "BLOCK"), 
    (6, 8080, "ALLOW")
]

result = find_conflicting_ports(rules)
print(f"Conflicts: {result}")

rules2 = [
    (1, 80, "ALLOW"), 
    (2, 80, "ALLOW"), 
    (3, 443, "BLOCK")
]

result2 = find_conflicting_ports(rules2)
print(f"Conflicts: {result2}")
