#!/usr/bin/python
"""Smallest multiple

   2520 is the smallest number that can be divided by each of the numbers from
   1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the
   numbers from 1 to 20?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import factor

factors = [0] * 20
accum = 1
for i in xrange(1, 21):
    for p,k in factor(i, [2,3,5,7,11,13,17,19]):
	if k > factors[p-1]:
	    accum *= p ** (k - factors[p-1])
	    factors[p-1] = k
print accum