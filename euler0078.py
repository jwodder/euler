#!/usr/bin/python
"""Coin partitions

   Let $p(n)$ represent the number of different ways in which $n$ coins can be
   separated into piles.  For example, five coins can separated into piles in
   exactly seven different ways, so $p(5)=7$.

	   OOOOO
	  OOOO O
	  OOO OO
	 OOO O O
	 OO OO O
	OO O O O
       O O O O O

   Find the least value of $n$ for which $p(n)$ is divisible by one million."""

from eulerlib import partitionNums

__tags__ = [
    'partitions',
    'partitions of unlabeled elements into unlabeled bins',
    'integer partition',
    'divisibility',
]

def solve():
    for n,pn in enumerate(partitionNums()):
        if pn % 1000000 == 0:
            return n

if __name__ == '__main__':
    print solve()
