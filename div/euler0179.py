#!/usr/bin/python
"""Consecutive positive divisors

   Find the number of integers $1 < n < 10^7$, for which $n$ and $n + 1$ have
   the same number of positive divisors.  For example, 14 has the positive
   divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15."""

limit = 10**7
divqtys = [1] * limit
qty = 0
for n in xrange(2, limit+1):
    for i in xrange(n, limit+1, n):
        divqtys[i-2] += 1
    if n > 2 and divqtys[n-3] == divqtys[n-2]:
        qty += 1
print qty
