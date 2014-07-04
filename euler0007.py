#!/usr/bin/python
import primes

p = primes.primeIter()
for _ in range(10000): p.next()
print p.next()
