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

ones = set([44,32,13,10,1])
eightyNines = set([85,89,145,42,20,4,16,37,58])

for i in xrange(2,10000000):
    chain = []
    j = i
    while j not in ones and j not in eightyNines:
	chain.append(j)
	j = sum(int(c)*int(c) for c in str(j))
    (ones if j in ones else eightyNines).update(chain)
print len(eightyNines)
