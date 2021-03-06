#!/usr/bin/python
"""Prime power triples

   The smallest number expressible as the sum of a prime square, prime cube,
   and prime fourth power is 28.  In fact, there are exactly four numbers below
   fifty that can be expressed in such a way:

       $28 = 2^2 + 2^3 + 2^4$
       $33 = 3^2 + 2^3 + 2^4$
       $49 = 5^2 + 2^3 + 2^4$
       $47 = 2^2 + 3^3 + 2^4$

   How many numbers below fifty million can be expressed as the sum of a prime
   square, prime cube, and prime fourth power?"""

from __future__ import division
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib   import primeIter

__tags__ = ['prime numbers']

bound=50000000

def solve():
    expressible = set()
    for p1 in primeIter(bound = bound**0.5):
        for p2 in primeIter(bound = bound**(1/3)):
            for p3 in primeIter(bound = bound**(1/4)):
                n = p1*p1 + p2*p2*p2 + p3*p3*p3*p3
                if n < bound:
                    expressible.add(n)
                else:
                    break
    return len(expressible)

if __name__ == '__main__':
    print solve()
