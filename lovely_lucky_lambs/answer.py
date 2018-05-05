from math import *

def answer(total_lambs):
    phi = (1 + sqrt(5)) / 2
    tau = (1 - sqrt(5)) / 2
    eps = pow(10, -10)

    generousList = int(round(log((total_lambs + 1) * sqrt(5)+eps, phi))) - 2
    fib_seq_nums = int(round((pow(phi, generousList+2)-pow(tau,generousList+2))/sqrt(5)))

    if total_lambs+1 < fib_seq_nums: generousList -= 1
    elif total_lambs + 1 == fib_seq_nums: total_lambs = fib_seq_nums

    if (total_lambs + 1) % 2 == 0: greedyList = int(round(log((total_lambs + 1), 2)))
    else: greedyList = int(log((total_lambs + 1), 2))

    return generousList - greedyList