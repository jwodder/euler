#!/usr/bin/python
r"""Totient maximum

    Euler's Totient function, $\varphi(n)$ [sometimes called the phi function],
    is used to determine the number of numbers less than $n$ which are
    relatively prime to $n$.  For example, as 1, 2, 4, 5, 7, and 8, are all
    less than nine and relatively prime to nine, $\varphi(9)=6$.

    $n$ | Relatively Prime | $\varphi(n)$ | $n/\varphi(n)$
    ----|------------------|--------------|---------------
    2   | 1                | 1            | 2
    3   | 1,2              | 2            | 1.5
    4   | 1,3              | 2            | 2
    5   | 1,2,3,4          | 4            | 1.25
    6   | 1,5              | 2            | 3
    7   | 1,2,3,4,5,6      | 6            | 1.1666...
    8   | 1,3,5,7          | 4            | 2
    9   | 1,2,4,5,7,8      | 6            | 1.5
    10  | 1,3,7,9          | 4            | 2.5

    It can be seen that $n=6$ produces a maximum $n/\varphi(n)$ for $n\leq 10$.

    Find the value of $n\leq 1,000,000$ for which $n/\varphi(n)$ is a
    maximum."""

# $n/\varphi(n)$ simplifies to $\prod_{p\mid n} \frac{p}{p-1}$, so in order to
# maximize this, we just need to cram as many prime numbers together as
# possible while keeping the product below 1000001 and giving preference to
# smaller primes (which have larger $\frac{p}{p-1}$ ratios).  Because
# multiplicities greater than 1 have no effect on $n/\varphi(n)$ and serve only
# to limit what other primes can be crammed into the result, each prime should
# be used no more than once.  Thus, we simply take the longest sequence of
# consecutive primes starting at 2 whose product is less than 1000001.

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib.oldprimes import primeIter

n = 1
for p in primeIter():
    np = n * p
    if np <= 1000000:
        n = np
    else:
        break
print n
