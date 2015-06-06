#!/usr/bin/python
"""Prime generating integers

   Consider the divisors of 30: 1,2,3,5,6,10,15,30.

   It can be seen that for every divisor $d$ of 30, $d+30/d$ is prime.

   Find the sum of all positive integers $n$ not exceeding 100 000 000 such
   that for every divisor $d$ of $n$, $d+n/d$ is prime."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib.primes import primeIter, factor, isPrime
from eulerlib import subsets, product

accum = 1
for n1 in primeIter(bound=100000000):
    if n1 == 2:
        continue
    n = n1 - 1
    fctrs = list(factor(n))
    assert fctrs[0][0] == 2
    if all(k == 1 for p,k in fctrs):
        primes = [p for p,k in fctrs]
        for subprimes in subsets(primes[1:]):
            n_2 = product(subprimes)
            if not isPrime(n_2 + n // n_2):
                break
        else:
            #print '%d\t%s' % (n, ','.join(map(str, primes)))
            accum += n
print accum
