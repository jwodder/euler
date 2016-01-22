#!/usr/bin/python
"""Special Pythagorean triplet

   A Pythagorean triplet is a set of three natural numbers, $a<b<c$, for which,

   $$a^2 + b^2 = c^2$$

   For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

   There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.

   Find the product $abc$."""

# Assuming that the target triplet is a multiple of a smaller triplet (which it
# is), we only need to find one triplet whose sum divides 1000 and then
# multiply each element by the quotient.

from eulerlib import perfectSqrt

__tags__ = ['Pythagorean triples']

def solve():
    for a in xrange(1, 1000):
        for b in range(a+1, (1000-a+1)//2):
            c = perfectSqrt(a*a + b*b)
            if c is not None and 1000 % (a+b+c) == 0:
                return a*b*c * (1000 // (a+b+c))**3

if __name__ == '__main__':
    print solve()
