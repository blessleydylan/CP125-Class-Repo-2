def find_at_risk_departments(departments, threshold):
    at_risk = []
    
    for department, students in departments.items():
        scores = students.values()
        total_students = len(scores)
        
        below_count = sum(score < threshold for score in scores)
        
        if below_count > total_students / 2:
            at_risk.append(department)
    
    return sorted(at_risk)


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))
