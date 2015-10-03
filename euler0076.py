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

# See <https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas>

partitions = [1, 1, 2, 3, 5, 7]

for n in xrange(len(partitions), 101):
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

print partitions[-1]-1
