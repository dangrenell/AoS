import random
import matplotlib.pyplot as plt


def coin_flip_convergence_grapher(p):
    sequence = []
    partial_sums = []

    for i in range(1, 1001):
        HT = 1 if random.random() < p else 0
        sequence.append(HT)
        partial_sums.append(sum(sequence)/i)

    plt.plot(range(1, 1001), partial_sums)
    plt.title(f"1000 coin flips with heads probability {p}")
    plt.show()


coin_flip_convergence_grapher(0.3)
coin_flip_convergence_grapher(0.03)
