#!/usr/bin/python
"""Circular primes

   The number, 197, is called a circular prime because all rotations of the
   digits: 197, 971, and 719, are themselves prime.

   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
   71, 73, 79, and 97.

   How many circular primes are there below one million?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import isPrime2

qty = 2  # 2 and 5
for p in xrange(3, 1000000, 2):
    pstr = str(p)
    if all(c in '1379' for c in pstr) and isPrime2(p) \
        and all(isPrime2(int(pstr[i:] + pstr[:i]))
		for i in range(1, len(pstr))):
	qty += 1
print qty