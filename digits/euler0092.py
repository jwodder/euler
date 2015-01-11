#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Square digit chains

   A number chain is created by continuously adding the square of the digits in
   a number to form a new number until it has been seen before.

   For example,

       44 → 32 → 13 → 10 → **1** → **1**
       85 → **89** → 145 → 42 → 20 → 4 → 16 → 37 → 58 → **89**

   Therefore any chain that arrives at 1 or 89 will become stuck in an endless
   loop.  What is most amazing is that EVERY starting number will eventually
   arrive at 1 or 89.

   How many starting numbers below ten million will arrive at 89?"""

from collections import defaultdict

def digits(n):
    ds = []
    while n > 0:
        ds.append(n % 10)
        n //= 10
    ds.sort()
    return tuple(ds)

ones = set(map(digits, [44,32,13,10,1]))

eightyNines = defaultdict(set)
for n in [85,89,145,42,20,4,16,37,58]:
    eightyNines[digits(n)].add(n)

for i in xrange(2,10000000):
    j = digits(i)
    chain = [(j,i)]
    while j not in ones and j not in eightyNines:
        i = sum(d*d for d in j)
        j = digits(i)
        chain.append((j,i))
    if j in ones:
        ones.update(x for x,_ in chain)
    else:
        for x,y in chain:
            eightyNines[x].add(y)
print sum(len(s) for s in eightyNines.itervalues())
