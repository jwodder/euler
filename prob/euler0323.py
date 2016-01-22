#!/usr/bin/python
r"""Bitwise-OR operations on random integers

    Let $y_0, y_1, y_2, \ldots$ be a sequence of random unsigned 32 bit
    integers

    (i.e. $0\leq y_i < 2^{32}$, every value equally likely).

    For the sequence $x_{i}$ the following recursion is given:

    - $x_0$ = 0 and
    - $x_i = x_{i-1} | y_{i-1}$, for $i>0$. ($|$ is the bitwise-OR operator)

    It can be seen that eventually there will be an index $N$ such that $x_i =
    2^{32}-1$ (a bit-pattern of all ones) for all $i\geq N$.

    Find the expected value of $N$.

    Give your answer rounded to 10 digits after the decimal point."""

from fractions import Fraction
from eulerlib  import sprintFFraction

__tags__ = ['probability', 'expected value']

def pascalRow(n):
    c = 1
    yield c
    for r in xrange(n):
        c = c * (n-r) // (r+1)
        yield c

def solve():
    E = [Fraction(0)] + [None] * 32
    for n in xrange(1, 33):
        E[n] = (1 + sum(nCi*(1+E[i]) for i,nCi in zip(range(n), pascalRow(n))))\
                / ((1 << n) - 1)
    return sprintFFraction(10, E[32].numerator, E[32].denominator)

if __name__ == '__main__':
    print solve()
