#!/usr/bin/python
r"""The prime factorisation of binomial coefficients

    The binomial coefficient ${}^{10}C_3 = 120$.

    $120 = 2^3\times 3\times 5 = 2\times 2\times 2\times 3\times 5$, and $2 + 2
    + 2 + 3 + 5 = 14$.

    So the sum of the terms in the prime factorisation of ${}^{10}C_3$ is 14.

    Find the sum of the terms in the prime factorisation of
    ${}^{20000000}C_{15000000}$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter

n = 20000000
r = 15000000

def facdiv(n,p):
    """Returns the largest natural number $k$ such that $p^k$ divides $n!$ ($p$
       prime).  (I believe this algorithm is called "Legendre's Result.")"""
    k = 0
    pexp = p
    while pexp <= n:
        k += n // pexp
        pexp *= p
    return k

print sum(p * (facdiv(n,p) - facdiv(r,p) - facdiv(n-r,p))
          for p in primeIter(bound=n))
