#!/usr/bin/python
r"""Amicable chains

    The proper divisors of a number are all the divisors excluding the number
    itself.  For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.  As
    the sum of these divisors is equal to 28, we call it a perfect number.

    Interestingly the sum of the proper divisors of 220 is 284 and the sum of
    the proper divisors of 284 is 220, forming a chain of two numbers.  For
    this reason, 220 and 284 are called an amicable pair.

    Perhaps less well known are longer chains.  For example, starting with
    12496, we form a chain of five numbers:

    $$12496 \to 14288 \to 15472 \to 14536 \to 14264 (\to 12496 \to \ldots)$$

    Since this chain returns to its starting point, it is called an amicable
    chain.

    Find the smallest member of the longest amicable chain with no element
    exceeding one million."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import aliquot

longestLength = 0
smallestMember = None
seen = set()

for n in xrange(2, 1000001):
    if n in seen: continue
    chainIndices = {n: 0}
    i = 0
    while n > 1:
        n = aliquot(n)
        i += 1
        if n > 1000000: break
        # This ^^ technically doesn't comply with a _prima facie_
        # interpretation of the problem, but it makes the program terminate in
        # under a minute with the correct answer, so...
        if n in chainIndices:
            i2 = chainIndices[n]
            if i - i2 > longestLength:
                chain = [m for m,j in chainIndices.iteritems() if j >= i2]
                if all(m <= 1000000 for m in chain):
                    longestLength = i - i2
                    smallestMember = min(chain)
            break
        elif n in seen:
            break
        seen.add(n)
        chainIndices[n] = i
print smallestMember
