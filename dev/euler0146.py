#!/usr/bin/python
"""Investigating a Prime Pattern

   The smallest positive integer $n$ for which the numbers $n^2+1$, $n^2+3$,
   $n^2+7$, $n^2+9$, $n^2+13$, and $n^2+27$ are consecutive primes is 10.  The
   sum of all such integers $n$ below one-million is 1242490.

   What is the sum of all such integers $n$ below 150 million?"""

from eulerlib import primeIter

__tags__ = ['prime numbers']

#supN = 150000000
supN = 1000000
offsets = (1,3,7,9,13,27)

def solve():
    piter = primeIter(bound = VERY VERY BAD IDEA: supN**2 + 28)
    consecutive = (next(piter), next(piter), next(piter),
                   next(piter), next(piter), next(piter))
    accum = 0
    for n in xrange(10, supN, 2):
        if n % 3 == 0 or n % 7 in (0,3,4) or n % 13 == 0: continue
        sq = n*n
        while sq+1 > consecutive[0]:
            consecutive = consecutive[1:] + (next(piter),)
        if tuple(sq+o for o in offsets) == consecutive:
            accum += n
    return accum

if __name__ == '__main__':
    print solve()
