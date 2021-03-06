#!/usr/bin/python
r"""Largest integer divisible by two primes

    The largest integer $\leq 100$ that is only divisible by both the primes 2
    and 3 is 96, as $96=32*3=2^5*3$.  For two *distinct* primes $p$ and $q$ let
    $M(p,q,N)$ be the largest positive integer $\leq N$ only divisible by both
    $p$ and $q$ and $M(p,q,N)=0$ if such a positive integer does not exist.

    E.g. $M(2,3,100)=96$.

    $M(3,5,100)=75$ and not 90 because 90 is divisible by 2, 3 and 5.

    Also $M(2,73,100)=0$ because there does not exist a positive integer $\leq
    100$ that is divisible by both 2 and 73.

    Let $S(N)$ be the sum of all distinct $M(p,q,N)$.  $S(100)=2262$.

    Find $S(10 000 000)$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter

__tags__ = ['maximization', 'prime numbers', 'divisibility']

n = 10000000

def powers(p,n):
    pk = p
    while pk <= n:
        yield pk
        pk *= p

def last(seq):
    lastval = None
    for x in seq:
        lastval = x
    return x

def solve():
    accum = 0
    for p in primeIter(bound=n//2):
        ppows = list(powers(p,n))
        for q in primeIter(bound=min(p-1,n//p)):
            accum += max(pk * last(powers(q, n//pk))
                         for pk in ppows if q <= n//pk)
    return accum

if __name__ == '__main__':
    print solve()
