#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Totient Chains

    Let $φ$ be Euler's totient function, i.e. for a natural number $n$, $φ(n)$
    is the number of $k$, $1\leq k\leq n$, for which $\gcd(k,n) = 1$.

    By iterating $φ$, each positive integer generates a decreasing chain of
    numbers ending in 1.

    E.g. if we start with 5 the sequence 5,4,2,1 is generated.

    Here is a listing of all chains with length 4:

        5,4,2,1
        7,6,2,1
        8,4,2,1
        9,6,2,1
        10,4,2,1
        12,4,2,1
        14,6,2,1
        18,6,2,1

    Only two of these chains start with a prime, their sum is 12.

    What is the sum of all primes less than 40000000 which generate a chain of
    length 25?"""

import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter, totient

def length25(p):
    x = p-1
    i = 2
    while x != 1 and i <= 25:
        x = totient(x)
        i += 1
    return i == 25

print sum(itertools.ifilter(length25, primeIter(bound=40000000)))
