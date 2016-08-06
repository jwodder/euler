#!/usr/bin/python
"""Under The Rainbow

   70 colored balls are placed in an urn, 10 for each of the seven rainbow
   colors.

   What is the expected number of distinct colors in 20 randomly picked balls?

   Give your answer with nine digits after the decimal point (a.bcdefghij)."""

# The balls are labeled, and the selection is done at once (i.e., not one ball
# at a time) without replacement.

from math      import factorial
from itertools import groupby
from eulerlib  import sprintFFraction, nCr, product

__tags__ = ['probability', 'expected value', 'urn problem',
            'drawing without replacement']

def partitions():
    def gen(left, bound, slots):
        """Returns an iterable of the ways to divide `left` unlabeled items
           into `slots` unsorted slots with no slot having more than `bound`
           items"""
        if left == 0:
            yield (0,) * slots
        elif slots != 0:
            for i in xrange(min(bound, left)+1):
                for uc in gen(left-i, i, slots-1):
                    yield (i,) + uc
    return gen(20, 10, 7)

def solve():
    colorsum = 0
    qty = 0
    fac7 = factorial(7)
    for spectrum in partitions():
        weight = product(nCr(10,c) for c in spectrum) * fac7 // \
            product(factorial(len(list(gr))) for _, gr in groupby(spectrum))
        colorsum += sum(1 for c in spectrum if c>0) * weight
        qty += weight
    #assert qty == nCr(70,20)
    return sprintFFraction(9, colorsum, qty)

if __name__ == '__main__':
    print solve()
