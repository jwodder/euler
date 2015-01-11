#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Digit factorial chains

   The number 145 is well known for the property that the sum of the factorial
   of its digits is equal to 145:

   $$1! + 4! + 5! = 1 + 24 + 120 = 145$$

   Perhaps less well known is 169, in that it produces the longest chain of
   numbers that link back to 169; it turns out that there are only three such
   loops that exist:

       169 → 363601 → 1454 → 169
       871 → 45361 → 871
       872 → 45362 → 872

   It is not difficult to prove that EVERY starting number will eventually get
   stuck in a loop.  For example,

       69 → 363600 → 1454 → 169 → 363601 (→ 1454)
       78 → 45360 → 871 → 45361 (→ 871)
       540 → 145 (→ 145)

   Starting with 69 produces a chain of five non-repeating terms, but the
   longest non-repeating chain with a starting number below one million is
   sixty terms.

   How many chains, with a starting number below one million, contain exactly
   sixty non-repeating terms?"""

facs = (1,)
for i in xrange(9):
    facs += (facs[-1] * (i+1),)

lengths = {1: 1, 2: 1, 145: 1, 40585: 1,
           169: 3, 363601: 3, 1454: 3,
           871: 2, 45361: 2,
           872: 2, 45362: 2}

qty = 0
for i in xrange(3, 1000000):
    chain = []
    j = i
    while j not in lengths:
        chain.append(j)
        j = sum(facs[int(c)] for c in str(j))
    l = lengths[j]
    for k in reversed(chain):
        l += 1
        lengths[k] = l
        if l == 60 and k < 1000000:
            qty += 1
print qty
