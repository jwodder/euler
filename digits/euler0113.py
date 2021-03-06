#!/usr/bin/python
"""Non-bouncy numbers

   Working from left-to-right if no digit is exceeded by the digit to its left
   it is called an increasing number; for example, 134468.

   Similarly if no digit is exceeded by the digit to its right it is called a
   decreasing number; for example, 66420.

   We shall call a positive integer that is neither increasing nor decreasing a
   "bouncy" number; for example, 155349.

   As $n$ increases, the proportion of bouncy numbers below $n$ increases such
   that there are only 12951 numbers below one-million that are not bouncy and
   only 277032 non-bouncy numbers below $10^{10}$.

   How many numbers below a googol ($10^{100}$) are not bouncy?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import memoize

__tags__ = ['digits', 'bouncy number']

@memoize
def partit(n,g):
    """Returns the number of possible partitions of `n` unlabelled objects into
       `g` (empty or non-empty) labelled groups"""
    if n == 0:
        return 1
    elif g == 1:
        return 1
    elif g == 2:
        return n+1
    else:
        return sum(partit(n-i, g-1) for i in xrange(n+1))

def solve():
    qty = 0
    maxDigits = 100
    for digits in xrange(1, maxDigits+1):
        p = partit(digits, 9)
        qty += p + (p - 9) + p * (maxDigits - digits)
        # - `p` increasing numbers with `digits` digits
        # - `p` decreasing numbers with `digits` digits and no trailing zeroes
        # - 9 `digits`-digit numbers that are both increasing and decreasing
        # - `p * (maxDigits - digits)` decreasing numbers with at most
        #   `maxDigits` digits, `digits` leading nonzero digits, and at least
        #   one trailing zero digit
    return qty

if __name__ == '__main__':
    print solve()
