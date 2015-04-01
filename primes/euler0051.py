#!/usr/bin/python
"""Prime digit replacements

   By replacing the 1st digit of the 2-digit number *3, it turns out that six
   of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

   By replacing the 3rd and 4th digits of 56**3 with the same digit, this
   5-digit number is the first example having seven primes among the ten
   generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
   56773, and 56993.  Consequently 56003, being the first member of this
   family, is the smallest prime with this property.

   Find the smallest prime which, by replacing part of the number (not
   necessarily adjacent digits) with the same digit, is part of an eight prime
   value family."""

from   itertools import combinations
import sys
sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib  import primeIter, isPrime

for p in primeIter():
    pstr = str(p)
    for d in '012':
        indices = [i for i,c in enumerate(pstr) if c == d]
        if indices:
            for sz in range(1, len(indices)+1):
                for subdex in combinations(indices, sz):
                    qty = 1
                    for d2 in range(int(d)+1, 10):
                        s2 = pstr
                        for i in subdex:
                            s2 = s2[:i] + str(d2) + s2[i+1:]
                        if isPrime(int(s2)):
                            qty += 1
                            if qty == 8:
                                print p
                                sys.exit()
