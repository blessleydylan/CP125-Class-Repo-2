def match_specialists(candidates_list, project_requirements):
    skill_frequency = {}

    for name, skills in candidates_list:
        for skill in skills:
            if skill not in skill_frequency:
                skill_frequency[skill] = 0
            skill_frequency[skill] += 1

    rare_skills_set = set()

    for skill, count in skill_frequency.items():
        if count < 3:
            rare_skills_set.add(skill)

    specialists = []

    for name, skills in candidates_list:
            if project_requirements.issubset(skills):
                 candidate_rare_skills = skills & rare_skills_set

                 if len(candidate_rare_skills) > 0:
                      specialists.append((name, candidate_rare_skills))

    return sorted(specialists)