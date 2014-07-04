#!/usr/bin/python
import sys
import primes

n = 600851475143

for p in primes.primeIter():
    while n % p == 0:
	n //= p
	if n == 1:
	    print p
	    sys.exit()
