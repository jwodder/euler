#!/usr/bin/python
"""Generalised Hamming Numbers

   A Hamming number is a positive number which has no prime factor larger than
   5.
   
   So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.

   There are 1105 Hamming numbers not exceeding $10^8$.

   We will call a positive number a generalised Hamming number of type $n$, if
   it has no prime factor larger than $n$.
   
   Hence the Hamming numbers are the generalised Hamming numbers of type 5.

   How many generalised Hamming numbers of type 100 are there which don't
   exceed $10^9$?"""

from collections import deque
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib    import primeIter

limit = 1000000000
primes = tuple(primeIter(bound=100))

qty = 1
queue = deque([(1,0)])
while queue:
    (n, pi) = queue.popleft()
    for j in xrange(pi, len(primes)):
	m = n * primes[j]
	if m <= limit:
	    queue.append((m,j))
	    qty += 1
print qty
