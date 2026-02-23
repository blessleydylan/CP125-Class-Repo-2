def match_specialists(candidates_list, project_requirements):
    count_map = {}

    for skill in project_requirements:
        if skill in count_map:
            count_map[skill] += 1
        else:
            count_map[skill] = 1
    print(count_map)

match_specialists(["Ali", {"Python", "Git"}],)