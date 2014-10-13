#!/usr/bin/python
r"""Prime square remainders

    Let $p_n$ be the $n$th prime: 2, 3, 5, 7, 11, ..., and let $r$ be the
    remainder when $(p_n-1)^n + (p_n+1)^n$ is divided by $p_n^2$.

    For example, when $n = 3$, $p_3 = 5$, and $4^3 + 6^3 = 280 \equiv 5
    \pmod{25}$.

    The least value of $n$ for which the remainder first exceeds $10^9$ is
    7037.

    Find the least value of $n$ for which the remainder first exceeds
    $10^{10}$."""

# From euler0120.py, we know that even values of $n$ should be skipped and that
# the remainder is congruent to $2np_n$ for odd $n$.  Moreover, because $2n <
# p_n$ at the values of $n$ under consideration, $2np_n < p_n^2$, and so the
# remainder actually equals $2np_n$.

from eulerlib import primeIter

piter = primeIter()
p = piter.next()
n = 1
while 2 * n * p <= 10**10:
    piter.next()
    p = piter.next()
    n += 2
print n
