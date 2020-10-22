import random
from math import isclose

A = {2, 4, 6}
B = {1, 2, 3, 4}


def cond_prob_emp(A, B, exps):
    A = set(A)
    B = set(B)
    AB = A & B

    A_hat = 0
    B_hat = 0
    AB_hat = 0

    exps = 100000

    for _ in range(exps):
        r = random.randint(1, 6)
        if r in A:
            A_hat += 1
        if r in B:
            B_hat += 1
        if r in AB:
            AB_hat += 1

    return isclose(AB_hat/exps, A_hat/exps * B_hat/exps, rel_tol=exps**0.5)


print(cond_prob_emp(A, B, 1000))
