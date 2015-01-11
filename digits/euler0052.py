#!/usr/bin/python
"""Permuted multiples

   It can be seen that the number, 125874, and its double, 251748, contain
   exactly the same digits, but in a different order.

   Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$,
   and $6x$, contain the same digits."""

# The first digit of $x$ must be 1 (or 5 or greater?  Doesn't matter; the
# answer starts with 1 anyway).

# $x$ must have at least 6 digits.

# $x$ cannot end with 0.

import sys

def digitset(n): return ''.join(sorted(str(n)))

digits = 6
while True:
    for n in xrange(10**(digits-1), 2 * 10**(digits-1)):
        if n % 10 == 0: continue
        if digitset(2*n) == digitset(3*n) == digitset(4*n) == digitset(5*n) \
            == digitset(6*n):
            print n
            sys.exit()
    digits += 1
