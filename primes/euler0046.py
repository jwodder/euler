#!/usr/bin/python
r"""Goldbach's other conjecture

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    \begin{eqnarray*}
     9 & = & 7 + 2\times 1^2 \\
    15 & = & 7 + 2\times 2^2 \\
    21 & = & 3 + 2\times 3^2 \\
    25 & = & 7 + 2\times 3^2 \\
    27 & = & 19 + 2\times 2^2 \\
    33 & = & 31 + 2\times 1^2
    \end{eqnarray*}

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter, primeCache

# <https://github.com/jwodder/bitvector.py>
from os import environ
sys.path.insert(1, environ['HOME'] + '/work/GITHUB/bitvector')
from bitvector import bitvector

class OddVecBool(object):
    """A compressed list of bools that only stores values at odd indices"""

    def __init__(self): self.data = bitvector()

    def resizeForMax(self, n): self.data.setWidth((n-1) // 2 + 1)

    def setBit(self, i): self.data[(i-1) // 2] = True

    def findFalse(self, start, stop):
	x = self.data.find(False, (start-1)//2, (stop-1)//2)
	return 2*x + 1 if x != -1 else x


piter = primeIter()
piter.next()
piter.next()
writable = OddVecBool()
writable.resizeForMax(3 + 2*9)
writable.setBit(3)
writable.setBit(3 + 2*1)
writable.setBit(3 + 2*4)
writable.setBit(3 + 2*9)

while True:
    lastPrime = primeCache[-1]
    pnext = piter.next()
    writable.resizeForMax(pnext + 2*pnext*pnext)
    writable.setBit(pnext)
    for i in xrange(1, lastPrime+1):
	writable.setBit(pnext + 2*i*i)
    for j in primeCache:
	for i in xrange(lastPrime+1, pnext+1):
	    writable.setBit(j + 2*i*i)
    i = writable.findFalse(lastPrime, pnext)
    if i != -1:
	print i
	break
