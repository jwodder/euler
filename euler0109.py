#!/usr/bin/python
from itertools import combinations_with_replacement

scores  = [m*i for i in xrange(1,21) for m in (1,2,3)] + [25,50]
doubles = [2*i for i in xrange(1,21)] + [50]

qty = sum(1 for d in doubles if d < 100)
for d in doubles:
    qty += sum(1 for s in scores if s+d < 100)
    qty += sum(1 for (s1,s2) in combinations_with_replacement(scores, 2)
                 if s1+s2+d < 100)
print qty
