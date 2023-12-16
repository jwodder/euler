#!/usr/bin/python
"""Sum of a square and a cube

   Many numbers can be expressed as the sum of a square and a cube.  Some of
   them in more than one way.

   Consider the palindromic numbers that can be expressed as the sum of a
   square and a cube, both greater than 1, in **exactly** 4 different ways.

   For example, 5229225 is a palindromic number and it can be expressed in
   exactly 4 different ways:

   $2285^2 + 20^3$

   $2223^2 + 66^3$

   $1810^2 + 125^3$

   $1197^2 + 156^3$

   Find the sum of the five smallest such palindromic numbers."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import ascending_range

__tags__ = ['digits', 'palindromic number']

def solve():
    current = None
    runlen = 0
    accum = 0
    found = 0
    for x in ascending_range(lambda s,c: (s+2)**2 + (c+2)**3, 2):
        if x == current:
            runlen += 1
        else:
            if runlen == 4:
                accum += current
                found += 1
                if found == 5:
                    return accum
            current = None
            runlen = None
            xstr = str(x)
            if xstr == xstr[::-1]:
                current = x
                runlen = 1

if __name__ == '__main__':
    print solve()
