#!/usr/bin/python
"""Under The Rainbow

   70 colored balls are placed in an urn, 10 for each of the seven rainbow
   colors.

   What is the expected number of distinct colors in 20 randomly picked balls?

   Give your answer with nine digits after the decimal point (a.bcdefghij)."""

from eulerlib import sprintFFraction, nCr, product

def combinations():
    for r in xrange(11):
        for o in xrange(min(10, 20-r)+1):
            for y in xrange(min(10, 20-r-o)+1):
                for g in xrange(min(10, 20-r-o-y)+1):
                    for b in xrange(min(10, 20-r-o-y-g)+1):
                        for i in xrange(min(10, 20-r-o-y-g-b)+1):
                            v = 20-r-o-y-g-b-i
                            if v <= 10:
                                yield (r,o,y,g,b,i,v)

colorsum = 0
qty = 0
for spectrum in combinations():
    weight = product(nCr(10, c) for c in spectrum)
    colorsum += sum(1 for c in spectrum if c>0) * weight
    qty += weight

print sprintFFraction(9, colorsum, qty)
