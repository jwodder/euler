#!/usr/bin/python
from __future__ import division
from math       import sqrt, floor
from eulerlib   import isPerfectSquare

def sqrtCF_PQ(d):
    """Returns the P and Q values used in the calculation of the simple
       continued fraction representation of ``sqrt(d)``"""
    sqrtD = sqrt(d)
    P = 0
    Q = 1
    while True:
	yield (P,Q)
	a = int(floor((P + sqrtD) / Q))
	P = a * Q - P
	Q = (d - P*P) // Q  # It can be shown that Q evenly divides d - P*P

qty = 0
for n in xrange(2, 10000):
    if isPerfectSquare(n): continue
    pqs = {}
    i = 0
    for pq in sqrtCF_PQ(n):
	if pq in pqs:
	    if (i - pqs[pq]) % 2 == 1:
		qty += 1
	    break
	else:
	    pqs[pq] = i
	    i += 1
print qty
