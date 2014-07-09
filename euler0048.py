#!/usr/bin/python
"""The series, $1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317$.

   Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + ... +
   1000^{1000}$."""

modulus = 10**10
accum = 0
for i in xrange(1, 1001):
    accum = (accum + i**i) % modulus
print accum
