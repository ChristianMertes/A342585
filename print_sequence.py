#!/usr/bin/env python
"""script to generate the infinite series https://oeis.org/A342585 with an optional parameter as the stopping point"""
import sys
from collections import Counter
from itertools import count
import sys

def aupton(target: int):
    """adapted from Michael S. Branicky's code from Jun 12 2021"""
    num: int = 0
    alst: list[int] = [0]
    inventory: Counter[int] = Counter([0])
    yield 0
    for n in range(2, target + 1) if target > 1 else count(2):
        c = inventory[num]
        num = 0 if c == 0 else num + 1
        alst.append(c)
        inventory.update([c])
        yield c
#    return alst


if __name__ == '__main__':
    target: int = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    for i in aupton(target):
        print(i, end=', ')
    print('\x08\x08')
