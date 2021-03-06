#!/usr/bin/python
"""Largest prime factor

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import allprimes

__tags__ = ['prime numbers', 'factorization', 'maximization']

n = 600851475143

def solve():
    for p in allprimes():
        while n % p == 0:
            n //= p
            if n == 1:
                return p

if __name__ == '__main__':
    print solve()
