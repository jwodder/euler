#!/usr/bin/python
r"""Digital root sums of factorisations

    A composite number can be factored many different ways.

    For instance, not including multiplication by one, 24 can be factored in 7
    distinct ways:

        24 = 2x2x2x3
        24 = 2x3x4
        24 = 2x2x6
        24 = 4x6
        24 = 3x8
        24 = 2x12
        24 = 24

    Recall that the digital root of a number, in base 10, is found by adding
    together the digits of that number, and repeating that process until a
    number is arrived at that is less than 10.  Thus the digital root of 467 is
    8.

    We shall call a Digital Root Sum (DRS) the sum of the digital roots of the
    individual factors of our number.

    The chart below demonstrates all of the DRS values for 24.

    Factorisation | Digital Root Sum
    --------------|-----------------
    2x2x2x3       | 9
    2x3x4         | 9
    2x2x6         | 10
    4x6           | 10
    3x8           | 11
    2x12          | 5
    24            | 6

    The maximum Digital Root Sum of 24 is 11.

    The function $mdrs(n)$ gives the maximum Digital Root Sum of $n$.  So
    $mdrs(24)=11$.

    Find $\sum mdrs(n)$ for $1 < n < 1,000,000$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import sieve, divisors

__tags__ = ['maximization', 'digital root', 'factorization']

def droot(n):
    return n and (n % 9 or 9)

def solve():
    sieve(10**6)
    mdrs = [None] * 10**6
    mdrs[0] = 0  # to emulate the omission of 1 from factorizations
    accum = 0
    for n in xrange(2, 10**6):
        val = max(droot(d) + mdrs[n // d - 1] for d in divisors(n) if d != 1)
        accum += val
        mdrs[n-1] = val
    return accum

if __name__ == '__main__':
    print solve()
