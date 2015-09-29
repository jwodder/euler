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

# See <https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas>

partitions = [1, 1, 2, 3, 5, 7]

while partitions[-1] % 1000000 != 0:
    n = len(partitions)
    pn = 0
    k = 1
    while True:
        pentK = (3*k*k - k) // 2
        pentNegK = (3*k*k + k) // 2
        if n >= pentNegK:
            pn += (-1)**((-k-1)%2) * partitions[n-pentNegK]
        if n >= pentK:
            pn += (-1)**((k-1)%2) * partitions[n-pentK]
        else:
            break
        k += 1
    partitions.append(pn)

print len(partitions)-1
