def audit_zero_trust(baseline_set, current_log_list):
    # Convert logs to a set to remove duplicates
    current_set = set(current_log_list)

    # Authorized: present in both baseline and logs
    authorized = baseline_set & current_set

    # Alerts: seen in logs but not trusted
    alerts = current_set - baseline_set

    # Inactive: trusted but not seen in logs
    inactive = baseline_set - current_set

    return authorized, alerts, inactive

