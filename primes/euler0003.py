#!/usr/bin/python
"""Largest prime factor

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143?"""

import sys
import eulerlib

n = 600851475143

for p in eulerlib.primeIter():
    while n % p == 0:
	n //= p
	if n == 1:
	    print p
	    sys.exit()
