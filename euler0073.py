#!/usr/bin/python
r"""Counting fractions in a range

    Consider the fraction, $n/d$, where $n$ and $d$ are positive integers.  If
    $n<d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for $d\leq 8$ in ascending
    order of size, we get:

    $$1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, \mathbf{3/8, 2/5, 3/7}, 1/2, 4/7, 3/5,
    5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8$$

    It can be seen that there are 3 fractions between 1/3 and 1/2.

    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
    proper fractions for $d\leq 12,000$?"""

from eulerlib import divisors, sieve

def twixtQty(d):
    """Returns the number of (not necessarily reduced) fractions with a
       denominator of `d` between 1/3 and 1/2"""
    return (d+1) // 2 - (d // 3 + 1)

sieve(12000)
cache = [0,0,0,0] + [None] * 12001
qty = 0
for d in xrange(4, 12001):
    cache[d] = twixtQty(d) - sum(cache[div] for div in divisors(d) if div != d)
    qty += cache[d]
print qty
