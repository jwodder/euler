#!/usr/bin/python
"""Prime summations

   It is possible to write ten as the sum of primes in exactly five different
   ways:

       7 + 3
       5 + 5
       5 + 3 + 2
       3 + 3 + 2 + 2
       2 + 2 + 2 + 2 + 2

   What is the first value which can be written as the sum of primes in over
   five thousand different ways?"""

import bisect
import sys; sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib import primeIter

__tags__ = ['prime numbers', 'combinatorics', 'partitions', 'integer partition',
            'partitions of unlabeled elements into unlabeled bins']

cache = {}

def primesums(n):
    def subp(n,p):
        """Returns the number of ways `n` can be written as a sum of primes
           each of which is no greater than `p`"""
        if n == 0:
            return 1
        elif n < 2:
            return 0
        else:
            i = bisect.bisect(primes, min(n,p))
            if (n,i) not in cache:
                cache[(n,i)] = sum(subp(n-primes[j], primes[j])
                                   for j in xrange(i-1, -1, -1))
            return cache[(n,i)]
    return subp(n,n)

def solve():
    bound = 1000
    primes = list(primeIter(bound=bound))
    n = 2
    while primesums(n) <= 5000:
        n += 1
        if n >= bound:
            bound *= 10
            primes = list(primeIter(bound=bound))
    return n

if __name__ == '__main__':
    print solve()
