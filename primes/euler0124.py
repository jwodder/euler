#!/usr/bin/python
r"""Ordered radicals

    The radical of $n$, $rad(n)$, is the product of the distinct prime factors
    of $n$.  For example, $504 = 2^3\times 3^2\times 7$, so $rad(504) = 2\times
    3\times 7 = 42$.

    If we calculate $rad(n)$ for $1\leq n\leq 10$, then sort them on $rad(n)$,
    and sorting on $n$ if the radical values are equal, we get:

        **Unsorted**          **Sorted**
        $n$  $rad(n)$     $n$  $rad(n)$  $k$
         1      1          1      1       1
         2      2          2      2       2
         3      3          4      2       3
         4      2          8      2       4
         5      5          3      3       5
         6      6          9      3       6
         7      7          5      5       7
         8      2          6      6       8
         9      3          7      7       9
        10     10         10     10      10

    Let $E(k)$ be the $k$th element in the sorted $n$ column; for example,
    $E(4) = 8$ and $E(6) = 9$.

    If $rad(n)$ is sorted for $1\leq n\leq 100000$, find $E(10000)$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib import primeIter, generateAsc

__tags__ = ['radical', 'prime numbers', 'ordering', 'factorization']

bound = 100000
index = 10000

def solve():
    primes = tuple(primeIter(bound=bound))
    seen = 0

    def nextNodes(x):
        rad, ps, nextI = x
        if nextI < len(primes):
            nextP = primes[nextI]
            yield (rad*nextP, ps+[nextP], nextI+1)
            if ps:
                yield (rad//ps[-1] * nextP, ps[:-1]+[nextP], nextI+1)

    for (rad, ps, nextI) in generateAsc([(1,[],0)], nextNodes):
        expses = [rad]
        for p in ps:
            for x in expses[:]:
                x *= p
                while x <= bound:
                    expses.append(x)
                    x *= p
        seen += len(expses)
        if seen >= index:
            expses.sort()
            return expses[index - seen - 1]

if __name__ == '__main__':
    print solve()
