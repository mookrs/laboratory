def anagram_solution_1(s1, s2):
    alist = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok

print(anagram_solution_1('abcd', 'dcba'))
