#!/usr/bin/python
r"""Diophantine reciprocals II

    In the following equation $x$, $y$, and $n$ are positive integers.

    $$\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$$

    It can be verified that when $n = 1260$ there are 113 distinct solutions
    and this is the least value of $n$ for which the total number of distinct
    solutions exceeds one hundred.

    What is the least value of $n$ for which the number of distinct solutions
    exceeds four million?

    NOTE: This problem is a much more difficult version of Problem 108 and as
    it is well beyond the limitations of a brute force approach it requires a
    clever implementation."""

from eulerlib import all_factored, sieve, product

def solve():
    sieve(10**8)
    for n, fctrs in all_factored():
        print n  #####
        if product(k*2+1 for _,k in fctrs) // 2 + 1 > 4000000:
            return n

if __name__ == '__main__':
    print solve()
