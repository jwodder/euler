#!/usr/bin/python
"""A permutation is an ordered arrangement of objects.  For example, 3124 is
   one possible permutation of the digits 1, 2, 3 and 4.  If all of the
   permutations are listed numerically or alphabetically, we call it
   lexicographic order.  The lexicographic permutations of 0, 1 and 2 are:

       012   021   102   120   201   210

   What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
   5, 6, 7, 8 and 9?"""

p = list('0123456789')
for _ in range(999999):
    for i in range(len(p)-2, -1, -1):
	if p[i] < p[i+1]:
	    i2 = len(p)-1
	    while p[i] >= p[i2]:
		i2 -= 1
	    p[i], p[i2] = p[i2], p[i]
	    p[i+1:] = reversed(p[i+1:])
	    break
print ''.join(p)
