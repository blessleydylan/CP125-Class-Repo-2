def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    courses = set()

    for s_id, course in enrollments:
        if s_id == student_id:
            courses.add(course)
    return courses

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    missing = required_courses - completed_courses
    return missing

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (missing_count, student_id) for students with missing courses."""
    report = []

    for student_id in students:
        completed_courses = get_student_courses(enrollments, student_id)
        missing_courses = find_missing_courses(completed_courses, required_courses)

        if len(missing_courses) > 0:
            report.append((len(missing_courses), student_id))
    report.sort(reverse=True)

    return report

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    students = set()

    for student_id, course in enrollments:
        students.add(student_id)

    return build_student_report(students, enrollments, required_courses) 

