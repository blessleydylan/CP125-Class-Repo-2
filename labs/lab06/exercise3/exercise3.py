def audit_blocklists(list_a, list_b, list_c):
    uni = list_a & list_b & list_c

    red = (list_a & list_b) | (list_b & list_c) | (list_a & list_c)

    uoa = list_a - (list_b | list_c)

    return uni, red, uoa

