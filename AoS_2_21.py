import random

p = 0.3
ns = (10, 100, 1000)


def empirical_theoretical_comp(p, n):
    num_heads = 0

    for _ in range(n):
        num_heads += 1 if random.random() < p else 0

    print("Actual number of heads:", num_heads)
    print("Theoretical number of heads:", p*n)


for n in ns:
    empirical_theoretical_comp(p, n)
    print()
