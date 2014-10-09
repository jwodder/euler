#!/usr/bin/python
"""Large non-Mersenne prime

   The first known prime found to exceed one million digits was discovered in
   1999, and is a Mersenne prime of the form $2^{6972593}-1$; it contains
   exactly 2,098,960 digits.  Subsequently other Mersenne primes, of the form
   $2^p-1$, have been found which contain more digits.

   However, in 2004 there was found a massive non-Mersenne prime which contains
   2,357,207 digits: $28433\times 2^{7830457}+1$.

   Find the last ten digits of this prime number."""

base = 10**10
exp = 7830457
a = 2
i=1
while not (exp & i):
    a = (a*a) % base
    i <<= 1
b = a
i <<= 1
a = (a*a) % base
while i <= exp:
    if exp & i: b = (b*a) % base
    i <<= 1
    a = (a*a) % base
print '%010d' % ((28433 * b + 1) % base,)
