#!/usr/bin/python
r"""Diophantine reciprocals I

    In the following equation $x$, $y$, and $n$ are positive integers.

    $$\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$$

    For $n = 4$ there are exactly three distinct solutions:

    $$\frac{1}{5} + \frac{1}{20} = \frac{1}{4}$$
    $$\frac{1}{6} + \frac{1}{12} = \frac{1}{4}$$
    $$\frac{1}{8} + \frac{1}{8} = \frac{1}{4}$$

    What is the least value of $n$ for which the number of distinct solutions
    exceeds one-thousand?

    NOTE: This problem is an easier version of Problem 110; it is strongly
    advised that you solve this one first."""

# Basic algebra shows that $1/x + 1/y = 1/n$ is equivalent to $y = xn/(x-n)$,
# and so once $n$ is fixed, we need only determine valid values of $x$.  As $y$
# must be an integer, $x-n$ must divide $xn$, and writing $k$ for $x-n$, we see
# that $k$ must divide $(n+k)n = n^2 + nk$, and so $k$ must divide $n^2$.
# Moreover, every positive divisor $k$ of $n^2$ produces an $x = n+k$ such that
# $x-n$ divides $xn$, and so the possible values of $x$ in $1/x + 1/y = 1/n$
# are precisely the positive integers that divide $n^2$.

from eulerlib import factor, product

n = 1
while product(k*2+1 for _,k in factor(n)) // 2 + 1 <= 1000:
    n += 1
print n
