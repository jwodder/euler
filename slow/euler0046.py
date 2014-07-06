#!/usr/bin/python
r"""It was proposed by Christian Goldbach that every odd composite number can
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

import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter

class OddList(object):
    """A compressed list that only stores values at odd indices.  It also
       auto-expands!"""

    def __init__(self):
	self.data = []

    def __getitem__(self, i):
	i = (i-1)//2
	if i < len(self.data): return self.data[i]
	else: return False

    def __setitem__(self, i, x):
	i = (i-1)//2
	if i < len(self.data): self.data[i] = x
	else:
	    self.data.extend([False] * (len(self.data) - i))
	    self.data.append(x)


piter = primeIter()
piter.next()
piter.next()
primes = [3]

writable = OddList()
writable[3] = True
writable[3 + 2*1] = True
writable[3 + 2*4] = True
writable[3 + 2*9] = True

while True:
    lastPrime = primes[-1]
    pnext = piter.next()
    for p in primes:
	for i in xrange(lastPrime+1, pnext+1):
	    writable[p + 2*i*i] = True
    primes.append(pnext)
    for i in xrange(1, pnext+1):
	writable[pnext + 2*i*i] = True
    for i in xrange(lastPrime, pnext, 2):
	if not writable[i]:
	    print i
	    sys.exit()
