#!/usr/bin/python
"""Pandigital prime

   We shall say that an $n$-digit number is pandigital if it makes use of all
   the digits 1 to $n$ exactly once.  For example, 2143 is a 4-digit pandigital
   and is also prime.

   What is the largest $n$-digit pandigital prime that exists?"""

# All 2, 3, 5, 6, 8, and 9 pandigital numbers are divisible by 3, and the only
# 1-pandigital is 1.  This leaves the 4 and 7 pandigitals.

from itertools import permutations, chain  # requires Python v.2.6+
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib  import isPrime

for pd in chain(permutations('7654321'), permutations('4321')):
    pd = int(''.join(pd))
    if isPrime(pd):
	print pd
	break
