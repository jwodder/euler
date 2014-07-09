#!/usr/bin/python
"""If $p$ is the perimeter of a right angle triangle with integral length
   sides, {a,b,c}, there are exactly three solutions for $p = 120$.

   {20,48,52}, {24,45,51}, {30,40,50}

   For which value of $p\leq 1000$, is the number of solutions maximised?"""

maxP = 0
maxSolv = 0
for p in xrange(3, 1001):
    qty = 0
    for a in xrange(1, (p+2)//3):
	for b in xrange((p-a-a+1)//2 + 1, (p-a+1)//2):
	    # c < a+b
	    # .: (p-2a)/2 < b
	    # b < c
	    # .: b < (p-a)/2
	    c = p - a - b
	    if a*a + b*b == c*c:
		qty += 1
    if qty > maxSolv:
	maxP = p
	maxSolv = qty
print maxP
