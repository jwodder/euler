#!/usr/bin/python
"""Counting summations

   It is possible to write five as a sum in exactly six different ways:

   4 + 1
   3 + 2
   3 + 1 + 1
   2 + 2 + 1
   2 + 1 + 1 + 1
   1 + 1 + 1 + 1 + 1

   How many different ways can one hundred be written as a sum of at least two
   positive integers?"""

cache = [[0]*100 for _ in xrange(101)]

def partitionQty(qty, mx):
    """Returns the number of ways `qty` can be written as a sum of integers each
       no greater than `mx`"""
    if cache[qty][mx] == 0:
	if qty == 0:
	    cache[qty][mx] = 1
	else:
	    cache[qty][mx] = sum(partitionQty(qty-i, i)
				 for i in range(min(qty, mx), 0, -1))
    return cache[qty][mx]

print partitionQty(100, 99)
