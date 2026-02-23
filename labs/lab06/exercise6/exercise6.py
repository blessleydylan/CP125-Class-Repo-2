def manage_roster(enrolled, drop_requests, waitlist):
    for student in drop_requests:
        enrolled.discard(student)

    if len(enrolled) < 5:
        while len(enrolled) < 7 and len(waitlist) > 0:
            enrolled.add(waitlist.pop())

    return len(enrolled)
