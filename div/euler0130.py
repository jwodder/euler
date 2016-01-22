#!/usr/bin/python
"""Composites with prime repunit property

   A number consisting entirely of ones is called a repunit.  We shall define
   $R(k)$ to be a repunit of length $k$; for example, R(6) = 111111.

   Given that $n$ is a positive integer and $GCD(n, 10) = 1$, it can be shown
   that there always exists a value, $k$, for which $R(k)$ is divisible by $n$,
   and let $A(n)$ be the least such value of $k$; for example, $A(7) = 6$ and
   $A(41) = 5$.

   You are given that for all primes, $p>5$, that $p-1$ is divisible by $A(p)$.
   For example, when $p = 41$, $A(41) = 5$, and 40 is divisible by 5.

   However, there are rare composite values for which this is also true; the
   first five examples being 91, 259, 451, 481, and 703.

   Find the sum of the first twenty-five composite values of $n$ for which
   $GCD(n, 10) = 1$ and $n-1$ is divisible by $A(n)$."""

from itertools import count, islice
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib  import isPrime, sieve

__tags__ = ['divisibility', 'repunit']

def A(n):
    k = 1
    rk_n = 1
    while rk_n != 0:
        k += 1
        rk_n = (rk_n * 10 + 1) % n
    return k

def answers():
    for n in count(3):
        if n % 2 and n % 5 and (n-1) % A(n) == 0 and not isPrime(n):
            yield n

def solve():
    sieve(10**6)  # just a guess
    return sum(islice(answers(), 25))

if __name__ == '__main__':
    print solve()
