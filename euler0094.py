#!/usr/bin/python
# -*- coding: utf-8 -*-
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

# We must find all triangles with integral sides x,x,y where x = y+d, d∈{1,-1},
# such that the area A = yh/2 = y/2 √(x^2 - (y/2)^2) is an integer.  This last
# expression equals y/4 √(3x^2 + 2xd - d^2); let k = 3x^2 + 2xd - d^2.  If x is
# even, then both y and k are odd, and so A is not an integer; therefore, x
# must be odd, and y and k must be even (and y/2 must be an integer).
# Moreover, in order for A to be an integer, k must be a perfect square, and as
# k is also even, it must be a multiple of 4, and so h = √(k/4) is an integer.
# Hence, (y/2, h, x) is a Pythagorean triple, and as gcd(x, y/2) = gcd(2y/2 ±
# 1, y/2) = 1, it must be primitive.  Thus, there exist coprime positive
# integers m,n such that m-n is positive & odd that satisfy:
#     y/2 or h   = m^2 - n^2
#     h   or y/2 = 2mn
#     z          = m^2 + n^2

# When y/2 = m^2-n^2 and h = 2mn, substituting into x = y+d and rearranging
# yields 3n^2 = m^2 + d; it is thus necessary that (m^2+d)/3 is an integer & a
# perfect square, and as m^2 mod 3 must be either 0 or 1, d must be -1.  It can
# be shown that any positive integer m>1 such that n = √((m^2-1)/3) is an
# integer is sufficient to produce an integral almost equilateral triangle;
# this is left as an exercise for the reader.  The triangle will have perimeter
# 4m^2, and so only the values of m less than or equal to √25e7 = 5000√10 will
# produce a triangle with perimeter not exceeding a billion.

for m in xrange(2, int(ceil(5000 * sqrt(10)))):
    n = m*m - 1
    if n % 3 == 0:
        n = perfectSqrt(n // 3)
        if n is not None:
            accum += 4 * m * m

# When y/2 = 2mn and h = m^2-n^2, substituting into x = y+d and rearranging
# yields n^2 - 4mn + m^2 - d = 0; it is thus necessary that n = 2m ± √(3m^2+d)
# is an integer less than m, and this latter requirement restricts us to only
# considering n = 2m - √(3m^2+d).  Moreover, as 3m^2+d must be a perfect
# square, modular arithmetic tells us that d must be 1.  It can be shown that
# any positive integer m>1 such that n = 2m - √(3m^2+1) is an integer is
# sufficient to produce an integral almost equilateral triangle; this is left
# as an exercise for the reader.  The triangle will have perimeter 12mn + 2,
# and so only the values of m less than or equal to √((1e9+2)/(23 - 12√3)) will
# produce a triangle with perimeter not exceeding a billion.

for m in xrange(2, int(ceil(sqrt(1000000002/(24 - 12 * sqrt(3)))))):
    n = perfectSqrt(3*m*m + 1)
    if n is not None:
        n = 2 * m - n
        accum += 12 * m * n + 2

print accum
