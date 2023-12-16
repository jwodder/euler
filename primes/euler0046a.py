#!/usr/bin/python
r"""Goldbach's other conjecture

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    \begin{eqnarray*}
     9 & = & 7 + 2\times 1^2 \\
    15 & = & 7 + 2\times 2^2 \\
    21 & = & 3 + 2\times 3^2 \\
    25 & = & 7 + 2\times 3^2 \\
    27 & = & 19 + 2\times 2^2 \\
    33 & = & 31 + 2\times 1^2
    \end{eqnarray*}

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib import allprimes, ascending_range

__tags__ = ['prime numbers']

primelist = []
piter = allprimes()

def pth(n):
    while n <= len(primelist):
        primelist.append(next(piter))
    return primelist[n]

def solve():
    i = 3
    for n in ascending_range(lambda x,y: pth(x) + 2*y*y, 2):
        if n > i:
            return i
        elif n == i:
            i += 2

if __name__ == '__main__':
    print solve()
