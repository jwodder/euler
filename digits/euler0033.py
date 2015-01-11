#!/usr/bin/python
r"""Digit canceling fractions

    The fraction $\frac{49}{98}$ is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    $\frac{49}{98} = \frac{4}{8}$, which is correct, is obtained by cancelling
    the 9s.

    We shall consider fractions like, $\frac{30}{50} = \frac{3}{5}$, to be
    trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import product, gcd

fractions = []

def checkFrac(ab,c,d, a2, b2):
    cd = c*10 + d
    if ab < cd and ab * b2 == cd * a2:
        fractions.append((a2, b2))

for a in range(1, 10):
    for b in range(1, 10):
        ab = a*10 + b
        for c in range(1, 10):
            checkFrac(ab,b,c, a,c)  # ab/bc = a/c
            checkFrac(ab,c,b, a,c)  # ab/cb = a/c
            checkFrac(ab,a,c, b,c)  # ab/ac = b/c
            checkFrac(ab,c,a, b,c)  # ab/ca = b/c

(nums, denoms) = zip(*fractions)
num = product(nums)
denom = product(denoms)
print denom // gcd(num, denom)
