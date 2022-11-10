#!/usr/bin/env python
"""
Script to generate a scatter plot of the infinite series https://oeis.org/A342585
with the number of terms to generate as the first parameter and the output file as a second.
"""
from collections import Counter
import sys
import matplotlib.pyplot as plt


def aupton(target: int):
    """adapted from Michael S. Branicky's code from Jun 12 2021"""
    num: int = 0
    alst: list[int] = [0]
    inventory: Counter[int] = Counter([0])
    for _ in range(2, target + 1):
        c = inventory[num]
        num = 0 if c == 0 else num + 1
        alst.append(c)
        inventory.update([c])
    return alst


if __name__ == '__main__':
    target: int = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
    plt.style.use('seaborn-v0_8')
    #plt.plot(aupton(target), 'bo')
    plt.scatter(range(1, target + 1), aupton(target), s=.1)
    plt.savefig(sys.argv[2] if len(sys.argv) > 2 else f'plot_up_to_{target}.png')
