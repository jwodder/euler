#!/usr/bin/python
"""Prime permutations

   The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
   increases by 3330, is unusual in two ways: (i) each of the three terms are
   prime, and, (ii) each of the 4-digit numbers are permutations of one
   another.

   There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
   primes, exhibiting this property, but there is one other 4-digit increasing
   sequence.

   What 12-digit number do you form by concatenating the three terms in this
   sequence?"""

from   collections import defaultdict
from   itertools   import dropwhile
import sys
sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib    import primeIter

primePerms = defaultdict(list)
for p in dropwhile(lambda n: n<1000, primeIter(bound=10000)):
    primePerms[''.join(sorted(str(p)))].append(p)

for perms in primePerms.itervalues():
    if len(perms) >= 3 and 1487 not in perms:
	for i,p1 in enumerate(perms[:-2]):
	    for j,p2 in enumerate(perms[i+1:-1]):
		p3 = p2 + p2 - p1
		if p3 in perms[j+i+2:]:
		    print '%d%d%d' % (p1, p2, p3)
		    sys.exit()
