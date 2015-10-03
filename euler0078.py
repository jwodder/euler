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

for n,pn in enumerate(partitionNums()):
    if pn % 1000000 == 0:
        print n
        break
