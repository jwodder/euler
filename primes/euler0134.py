#!/usr/bin/python
r"""Prime pair connection

    Consider the consecutive primes $p_1 = 19$ and $p_2 = 23$.  It can be
    verified that 1219 is the smallest number such that the last digits are
    formed by $p_1$ whilst also being divisible by $p_2$.

    In fact, with the exception of $p_1 = 3$ and $p_2 = 5$, for every pair of
    consecutive primes, $p_2 > p_1$, there exist values of $n$ for which the
    last digits are formed by $p_1$ and $n$ is divisible by $p_2$.  Let $S$ be
    the smallest of these values of $n$.

    Find $\sum S$ for every pair of consecutive primes with $5\leq p_1\leq
    1000000$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import modInverse, allprimes

__tags__ = ['prime numbers', 'digits', 'divisibility']

def solve():
    piter = allprimes()
    next(piter)
    next(piter)
    p1 = next(piter)
    p2 = next(piter)
    nextMag = 10
    accum = 0
    while p1 <= 1000000:
        while nextMag < p1:
            nextMag *= 10
        accum += p1 + nextMag * ((p2 - p1) * modInverse(nextMag, p2) % p2)
        (p1, p2) = (p2, next(piter))
    return accum

if __name__ == '__main__':
    print solve()
