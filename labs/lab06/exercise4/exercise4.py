def synchronize_databases(legacy_list, modern_set, blacklist):
    # Step 1: Sanitize legacy data (exclude blacklisted emails)
    sanitized_legacy_ids = {
        record_id
        for record_id, email in legacy_list
        if email not in blacklist
    }

    # Step 2: IDs lost during migration (in legacy but not in modern)
    lost_set = sanitized_legacy_ids - modern_set

    # Step 3: Ghost IDs (in modern but never existed in legacy)
    ghost_set = modern_set - sanitized_legacy_ids

    return lost_set, ghost_set

