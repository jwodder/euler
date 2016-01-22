#!/usr/bin/python
r"""Combinatoric selections

    There are exactly ten ways of selecting three from five, 12345:

    $$123, 124, 125, 134, 135, 145, 234, 235, 245, \mbox{ and } 345$$

    In combinatorics, we use the notation, ${}^5C_3 = 10$.

    In general,

    ${}^nC_r = \frac{n!}{r!(n-r)!}$, where $r\leq n$, $n! = n\times (n-1)\times
    \ldots\times 3\times 2\times 1$, and $0! = 1$.

    It is not until $n = 23$, that a value exceeds one-million: ${}^{23}C_{10}
    = 1144066$.

    How many, not necessarily distinct, values of ${}^nC_r$, for $1\leq n\leq
    100$, are greater than one-million?"""

from eulerlib import nCr

__tags__ = ['combination', 'binomial coefficients']

def solve():
    qty = 0
    r = 11  # smallest `r` such that `nCr(n,r) > 1000000`
    for n in xrange(23, 101):
        while nCr(n, r-1) > 1000000:
            r -= 1
        qty += n + 1 - 2*r
    return qty

if __name__ == '__main__':
    print solve()
