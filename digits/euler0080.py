#!/usr/bin/python
"""Square root digital expansion

   It is well known that if the square root of a natural number is not an
   integer, then it is irrational.  The decimal expansion of such square roots
   is infinite without any repeating pattern at all.

   The square root of two is 1.41421356237309504880..., and the digital sum of
   the first one hundred decimal digits is 475.

   For the first one hundred natural numbers, find the total of the digital
   sums of the first one hundred decimal digits for all the irrational square
   roots."""

def sqrtStr(n, digits=100):
    """Calculates the square root of an integer `n` as a string of at most
       `digits` digits (possibly containing a decimal point).

       Based on <http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation>"""
    if n < 0: raise ValueError('negative argument')
    nstr = str(n)
    if len(nstr) % 2 == 1: nstr = '0' + nstr
    dpairs = [int(nstr[i:i+2]) for i in range(0, len(nstr), 2)]
    s = ''
    p = 0
    c = 0
    pointed = False
    for _ in xrange(digits):
        if dpairs:
            leading = dpairs.pop(0)
        else:
            if not pointed:
                s += '.'
                pointed = True
            leading = 0
        c = c * 100 + leading
        for x in xrange(9, -1, -1):
            y = x * (20 * p + x)
            if y <= c: break
        p = p * 10 + x
        s += str(x)
        c -= y
        if c == 0 and not dpairs: return s
    return s

accum = 0
for n in xrange(1, 101):
    root = sqrtStr(n)
    if '.' in root:
        accum += sum(int(c) for c in root if c != '.')
print accum
