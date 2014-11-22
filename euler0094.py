#!/usr/bin/python
"""Almost equilateral triangles

   It is easily proved that no equilateral triangle exists with integral length
   sides and integral area.  However, the *almost equilateral triangle* 5-5-6
   has an area of 12 square units.

   We shall define an *almost equilateral triangle* to be a triangle for which
   two sides are equal and the third differs by no more than one unit.

   Find the sum of the perimeters of all *almost equilateral triangles* with
   integral side lengths and area and whose perimeters do not exceed one
   billion (1,000,000,000)."""

from math     import sqrt, ceil
from eulerlib import perfectSqrt

accum = 0

for m in xrange(2, int(ceil(5000 * sqrt(10)))):
    n = m*m - 1
    if n % 3 == 0:
	n = perfectSqrt(n // 3)
	if n is not None:
	    accum += 4 * m * m

for m in xrange(2, int(ceil(sqrt(1000000002/(24 - 12 * sqrt(3)))))):
    n = perfectSqrt(3*m*m + 1)
    if n is not None:
	n = 2 * m - n
	#assert m > n and (m-n) % 2 == 1 and gcd(m,n) == 1
	#assert m*m + n*n - 4*m*n in (1, -1)
	accum += 12 * m * n + 2

print accum
