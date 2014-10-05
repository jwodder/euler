#!/usr/bin/python
"""Generalised Hamming Numbers

   A Hamming number is a positive number which has no prime factor larger than
   5.
   
   So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.

   There are 1105 Hamming numbers not exceeding $10^8$.

   We will call a positive number a generalised Hamming number of type $n$, if
   it has no prime factor larger than $n$.
   
   Hence the Hamming numbers are the generalised Hamming numbers of type 5.

   How many generalised Hamming numbers of type 100 are there which don't
   exceed $10^9$?"""

import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter, cross, product

limit = 1000000000
primes = list(primeIter(bound=100))

primePowers = []
for p in primes:
    powers = [1]
    x = p
    while x <= limit:
	powers.append(x)
	x *= p
    primePowers.append(powers)

qty = 0

#for factors in cross(*primePowers):
#    if product(factors) <= limit:
#	qty += 1

indices = [0] * len(primePowers)
while True:
    x = product(powers[i] for (powers, i) in zip(primePowers, indices))
    if x <= limit:
	qty += 1
    else:
	for i in range(len(indices)-1, -1, -1):
	    if indices[i] == 0:
	        indices[i] = len(primePowers[i])
	    else:
	        indices[i] = len(primePowers[i])
		break
    for i in range(len(indices)-1, -1, -1):
	indices[i] += 1
	if indices[i] >= len(primePowers[i]):
	    indices[i] = 0
	else:
	    break
    else:
	break

print qty
