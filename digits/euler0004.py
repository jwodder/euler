#!/usr/bin/python
r"""Largest palindrome product

   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is $9009 = 91\times 99$.

   Find the largest palindrome made from the product of two 3-digit numbers."""

# Note: Assuming the largest palindrome is 6 digits long (which it is), it can
# be shown to be a multiple of 11, and thus at least one of its factors must be
# a multiple of 11.

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import ascending_range

__tags__ = ['digits', 'palindromic number', 'maximization']

def solve():
    for n in ascending_range(lambda i,j: (990 - 11*i) * (999 - j), 2,
                             keyfunc=lambda n: -n):
        ns = str(n)
        if ns == ns[::-1]:
            return ns

if __name__ == '__main__':
    print solve()
