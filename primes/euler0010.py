#!/usr/bin/python
"""Summation of primes

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter
print sum(primeIter(bound=2000000))
