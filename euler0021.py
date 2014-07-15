#!/usr/bin/python
r"""Amicable numbers

    Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less
    than $n$ which divide evenly into $n$).

    If $d(a) = b$ and $d(b) = a$, where $a\neq b$, then $a$ and $b$ are an
    amicable pair and each of $a$ and $b$ are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore $d(220) = 284$.  The proper divisors of 284 are 1, 2,
    4, 71 and 142; so $d(284) = 220$.

    Evaluate the sum of all the amicable numbers under 10000."""

from eulerlib import aliquot

calculated = set()
accum = 0
for i in xrange(2, 10001):
    if i in calculated: continue
    calculated.add(i)
    j = aliquot(i)
    if i != j and aliquot(j) == i:
	calculated.add(j)
	accum += i + j
print accum
