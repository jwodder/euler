#!/usr/bin/python
"""Circular primes

   The number, 197, is called a circular prime because all rotations of the
   digits: 197, 971, and 719, are themselves prime.

   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
   71, 73, 79, and 97.

   How many circular primes are there below one million?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter

potentials = set()
qty = 0

for p in primeIter(bound=1000000):
    pstr = str(p)
    if len(pstr) == 1 or pstr == '11':
	qty += 1
    elif not ('2' in pstr or '5' in pstr or '0' in pstr):
	ismax = True
	for i in range(1, len(pstr)):
	    p2 = pstr[i:] + pstr[:i]
	    if p2 < pstr and p2 not in potentials:
		break
	    elif p2 > pstr:
		ismax = False
	else:
	    if ismax:
		qty += len(pstr)
		for i in range(1, len(pstr)):
		    potentials.remove(pstr[i:] + pstr[:i])
	    else:
		potentials.add(pstr)
print qty
