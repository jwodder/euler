#!/usr/bin/python
"""10001st prime

   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6th prime is 13.

   What is the 10 001st prime number?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
import eulerlib

p = eulerlib.primeIter()
for _ in xrange(10000): p.next()
print p.next()
