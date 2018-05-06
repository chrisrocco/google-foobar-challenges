from itertools import combinations


def answer(num_buns, num_required):
    result_set = [[] for _ in range(num_buns)]
    for idx, combo in enumerate(combinations(range(num_buns), num_buns - num_required + 1)):
        for key in combo:
            result_set[key].append(idx)
    return result_set
