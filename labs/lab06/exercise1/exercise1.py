def filter_bots(bot_ids):
    """
    Returns a set of bot user IDs for fast membership checks.
    """
    return set(bot_ids)


def get_legit_power_users(log_data, bot_ids, threshold):
    # Prepare bot lookup
    bots = filter_bots(bot_ids)

    # Dictionary to store unique actions per user
    user_actions = {}

    for timestamp, user_id, action_type in log_data:
        # Skip bot users
        if user_id in bots:
            continue

        # Track unique actions
        if user_id not in user_actions:
            user_actions[user_id] = set()
        user_actions[user_id].add(action_type)

    # Identify power users
    power_users = [
        user_id
        for user_id, actions in user_actions.items()
        if len(actions) > threshold
    ]

    # Return sorted list
    return sorted(power_users)
