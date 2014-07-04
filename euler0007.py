#!/usr/bin/python
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6th prime is 13.

   What is the 10 001st prime number?"""

import primes

p = primes.primeIter()
for _ in range(10000): p.next()
print p.next()
