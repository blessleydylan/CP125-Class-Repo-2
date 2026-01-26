def clean_sessions(server_pool, active_sessions, dead_servers):
    """
    Removes all sessions connected to dead servers that exist in the server pool.
    Returns the remaining sessions sorted alphabetically by server ID.
    """

    # Validate dead servers against the server pool
    valid_dead_servers = {
        server for server in dead_servers if server in server_pool
    }

    # Filter out sessions connected to valid dead servers
    remaining_sessions = [
        session for session in active_sessions
        if session[0] not in valid_dead_servers
    ]

    # Sort remaining sessions by server ID
    remaining_sessions.sort(key=lambda session: session[0])

    return remaining_sessions
