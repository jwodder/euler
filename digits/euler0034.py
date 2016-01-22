#!/usr/bin/python
"""Digit factorials

   145 is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.

   Find the sum of all numbers which are equal to the sum of the factorial of
   their digits.

   Note: as $1! = 1$ and $2! = 2$ are not sums they are not included."""

# 9! = 362880, so once you get up to 7 digits, the sum of the factorial of
# digits will always be less than the starting number.

__tags__ = ['digits', 'sum of function of digits', 'factorial']

def solve():
    facs = (1,)
    for i in xrange(9):
        facs += (facs[-1] * (i+1),)
    accum = 0
    for i in xrange(10, 1000000):
        if i == sum(facs[int(c)] for c in str(i)):
            accum += i
    return accum

if __name__ == '__main__':
    print solve()
