#!/usr/bin/python
r"""Factorial digit sum

    $n!$ means $n\times(n-1)\times\cdots\times 3\times 2\times 1$

    For example, $10! = 10\times 9\times\cdots\times 3\times 2\times 1 =
    3628800$, and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 +
    8 + 0 + 0 = 27$.

    Find the sum of the digits in the number 100!"""

from math import factorial

__tags__ = ['digits', 'sum of digits', 'factorial']

def solve():
    return sum(int(c) for c in str(factorial(100)))

if __name__ == '__main__':
    print solve()
