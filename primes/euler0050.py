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
from eulerlib import primeIter, isPrime

maxPrime = 0
maxTerms = 0
primes = list(primeIter(bound=10**6))
for i,p in enumerate(primes):
    try:
        accum = sum(primes[i+j] for j in xrange(maxTerms))
    except IndexError:
        break
    if accum >= 1000000:
        break
    for j in xrange(maxTerms, len(primes)-i):
        accum += primes[i+j]
        if accum >= 1000000:
            break
        if isPrime(accum):
            maxPrime = accum
            maxTerms = j+1
print maxPrime
