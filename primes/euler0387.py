#!/usr/bin/python
"""Harshad Numbers

   A **Harshad or Niven number** is a number that is divisible by the sum of
   its digits.

   201 is a Harshad number because it is divisible by 3 (the sum of its
   digits.)

   When we truncate the last digit from 201, we get 20, which is a Harshad
   number.

   When we truncate the last digit from 20, we get 2, which is also a Harshad
   number.

   Let's call a Harshad number that, while recursively truncating the last
   digit, always results in a Harshad number a *right truncatable Harshad
   number.*

   Also:

   $201/3=67$ which is prime.

   Let's call a Harshad number that, when divided by the sum of its digits,
   results in a prime a *strong Harshad number*.

   Now take the number 2011 which is prime.

   When we truncate the last digit from it we get 201, a strong Harshad number
   that is also right truncatable.

   Let's call such primes *strong, right truncatable Harshad primes*.

   You are given that the sum of the strong, right truncatable Harshad primes
   less than 10000 is 90619.

   Find the sum of the strong, right truncatable Harshad primes less than
   $10^{14}$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import sieve, isPrime

sieve(10**7)
new = [(d,d) for d in range(1, 10)]
accum = 0
for _ in xrange(12):
    newer = []
    for n,s in new:
        for d in xrange(10):
            n2 = n*10 + d
            s2 = s + d
            q,r = divmod(n2, s2)
            if r == 0:
                newer.append((n2, s2))
                if isPrime(q, presieve=False):
                    for e in [1,3,7,9]:
                        m = n2 * 10 + e
                        if isPrime(m, presieve=False):
                            accum += m
    new = newer
print accum
