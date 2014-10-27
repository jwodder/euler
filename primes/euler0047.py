#!/usr/bin/python
r"""Distinct primes factors

    The first two consecutive numbers to have two distinct prime factors are:

    $$14 = 2\times 7$$
    $$15 = 3\times 5$$

    The first three consecutive numbers to have three distinct prime factors
    are:

    $$644 = 2^2\times 7\times 23$$
    $$645 = 3\times 5\times 43$$
    $$646 = 2\times 17\times 19.$$

    Find the first four consecutive integers to have four distinct prime
    factors.  What is the first of these numbers?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import factor

n = 1
streak = 0
while streak != 4:
    fctrs = len(list(factor(n)))
    if fctrs == 4:
	streak += 1
    else:
	streak = 0
    n += 1
print n-4
