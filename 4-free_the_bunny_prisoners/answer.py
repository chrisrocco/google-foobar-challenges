from itertools import combinations


def answer(num_buns, num_required):
    n = num_buns
    r = n - num_required + 1
    result_set = [[] for i in range(n)]
    for idx, combo in enumerate(combinations(range(n), r)):
        for key in combo:
            result_set[key].append(idx)
    return result_set
