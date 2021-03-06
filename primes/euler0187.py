#!/usr/bin/python
r"""Semiprimes

    A composite is a number containing at least two prime factors. For example,
    $15 = 3\times 5$; $9 = 3\times 3$; $12 = 2\times 2\times 3$.

    There are ten composites below thirty containing precisely two, not
    necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

    How many composite integers, $n<10^8$, have precisely two, not necessarily
    distinct, prime factors?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter

__tags__ = ['prime numbers', 'factorization']

def ilen(seq):
    return sum(1 for _ in seq)

n = 100000000

def solve():
    return sum(ilen(primeIter(bound=min(p,n//p))) for p in primeIter(bound=n//2))

if __name__ == '__main__':
    print solve()
