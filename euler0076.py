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

from eulerlib import partitionNums, nth

__tags__ = ['partitions','partitions of unlabeled elements into unlabeled bins',
            'integer partition']

def solve():
    return nth(partitionNums(), 100) - 1

if __name__ == '__main__':
    print solve()
