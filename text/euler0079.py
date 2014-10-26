#!/usr/bin/python
"""Passcode derivation

   A common security method used for online banking is to ask the user for
   three random characters from a passcode.  For example, if the passcode was
   531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
   reply would be: 317.

   The text file, `keylog.txt`, contains fifty successful login attempts.

   Given that the three characters are always asked for in order, analyse the
   file so as to determine the shortest possible secret passcode of unknown
   length."""

# Assume that no character is repeated in the passcode (which turns out to be
# correct)

from __future__  import with_statement
from collections import defaultdict

befores = defaultdict(set)
afters  = defaultdict(set)
allvals = set()

with open('../data/keylog.txt') as fp:
    for line in fp:
	a,b,c = line.strip()
	allvals.update([a,b,c])
	for x,y in ((a,b), (a,c), (b,c)):
	    afters[x].add(y)
	    for w in befores[x]:
		afters[w].add(y)
	    befores[y].add(x)
	    for z in afters[y]:
		befores[z].add(x)
print ''.join(sorted(allvals, key=lambda c: befores[c]))
