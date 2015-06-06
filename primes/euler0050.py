#!/usr/bin/python
"""Consecutive prime sum

   The prime 41, can be written as the sum of six consecutive primes:

   $$41 = 2 + 3 + 5 + 7 + 11 + 13$$

   This is the longest sum of consecutive primes that adds to a prime below
   one-hundred.

   The longest sum of consecutive primes below one-thousand that adds to a
   prime, contains 21 terms, and is equal to 953.

   Which prime, below one-million, can be written as the sum of the most
   consecutive primes?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib.oldprimes import primeIter, isPrime

maxPrime = 0
maxTerms = 0
for i,p in enumerate(primeIter()):
    if p*maxTerms >= 1000000: break
    piter2 = primeIter()
    for _ in xrange(i+1): piter2.next()
    accum = p
    for j,q in enumerate(piter2):
        accum += q
        if accum >= 1000000: break
        if j < maxTerms: continue
        if isPrime(accum):
            maxPrime = accum
            maxTerms = j+1
print maxPrime
