#!/usr/bin/python
"""Truncatable primes

   The number 3797 has an interesting property.  Being prime itself, it is
   possible to continuously remove digits from left to right, and remain prime
   at each stage: 3797, 797, 97, and 7.  Similarly we can work from right to
   left: 3797, 379, 37, and 3.

   Find the sum of the only eleven primes that are both truncatable from left
   to right and right to left.

   NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib.oldprimes import isPrime

leftTruncate  = set([2,3,5,7])
rightTruncate = set([2,3,5,7])
bothTruncate  = set()
magnitude = 1

while len(bothTruncate) < 11:
    magnitude *= 10
    lt2 = set()
    for p in leftTruncate:
        for d in xrange(1,10):
            x = d * magnitude + p
            if isPrime(x):
                lt2.add(x)
    leftTruncate = lt2
    rt2 = set()
    for p in rightTruncate:
        for d in (1,3,7,9):
            x = p * 10 + d
            if isPrime(x):
                rt2.add(x)
    rightTruncate = rt2
    bothTruncate.update(leftTruncate & rightTruncate)
print sum(bothTruncate)
