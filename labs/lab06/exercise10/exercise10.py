def get_unique_attendees(attendance_logs):
    """Extract set of all unique attendee IDs."""
    unique_attendees = set()
    for attendee_id, event_name in attendance_logs:
        unique_attendees.add(attendee_id)
    return unique_attendees

def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    unique_events = set()
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id:
            unique_events.add(event_name)
    event_count = len(unique_events)
    return event_count

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    qualified = []

    for attendee_id in attendees:
        event_count = count_unique_events(attendance_logs, attendee_id)

        if event_count >= min_events:
            qualified.append(attendee_id)
    qualified.sort()

    return qualified

def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    pass
    attendees = get_unique_attendees(attendance_logs)

    qualified_attendee = filter_by_threshold(attendees, attendance_logs, min_events)

    return qualified_attendee