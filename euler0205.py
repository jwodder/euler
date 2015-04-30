#!/usr/bin/python
"""Dice Game

   Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
   3, 4.

   Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4,
   5, 6.

   Peter and Colin roll their dice and compare totals: the highest total wins.
   The result is a draw if the totals are equal.

   What is the probability that Pyramidal Pete beats Cubic Colin?  Give your
   answer rounded to seven decimal places in the form 0.abcdefg"""

from collections import defaultdict
from eulerlib    import cross, sprintFFraction

# 9d4 > 6d6

peteRolls = defaultdict(int)
for roll in cross(*[range(1,5)]*9):
    peteRolls[sum(roll)] += 1

colinRolls = defaultdict(int)
for roll in cross(*[range(1,7)]*6):
    colinRolls[sum(roll)] += 1

prob = 0
denom = 6**6 * 4**9
for c in xrange(6, 37):
    colinProb = colinRolls[c]
    peteProb = sum(peteRolls[p] for p in xrange(c+1, 37))
    prob += colinProb * peteProb

print sprintFFraction(7, prob, denom)
