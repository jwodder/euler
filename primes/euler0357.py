#!/usr/bin/python
"""Prime generating integers

   Consider the divisors of 30: 1,2,3,5,6,10,15,30.

   It can be seen that for every divisor $d$ of 30, $d+30/d$ is prime.

   Find the sum of all positive integers $n$ not exceeding 100 000 000 such
   that for every divisor $d$ of $n$, $d+n/d$ is prime."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter, isPrime

__tags__ = ['divisibility', 'prime numbers']

def solve():
    accum = 0
    for n1 in primeIter(bound=100000000):
        n = n1 - 1
        for d in xrange(2, int(n**0.5)+1):
            if n % d == 0 and not isPrime(d + n // d):
                break
        else:
            accum += n
    return accum

if __name__ == '__main__':
    print solve()
