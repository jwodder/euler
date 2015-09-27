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

from eulerlib import memoize

@memoize
def partitionQty(qty, mx):
    """Returns the number of ways `qty` can be written as a sum of integers each
       no greater than `mx`"""
    if qty == 0:
        return 1
    else:
        return sum(partitionQty(qty-i, i) for i in range(min(qty, mx), 0, -1))

print partitionQty(100, 99)
