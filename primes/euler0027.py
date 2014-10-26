#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Quadratic primes

    Euler discovered the remarkable quadratic formula:

    $$n^2 + n + 41$$

    It turns out that the formula will produce 40 primes for the consecutive
    values $n = 0 \mbox{ to } 39$.  However, when $n = 40$, $40^2 + 40 + 41 =
    40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41$, $41^2 +
    41 + 41$ is clearly divisible by 41.

    The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80
    primes for the consecutive values $n = 0 \mbox{ to } 79$.  The product of
    the coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form:

	$n^2 + an + b$, where $|a| < 1000$ and $|b| < 1000$

	where $|n|$ is the modulus/absolute value of $n$
	e.g. $|11| = 11$ and $|-4| = 4$

    Find the product of the coefficients, $a$ and $b$, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of $n$, starting with $n = 0$."""

from itertools import dropwhile
from math      import sqrt
from eulerlib  import primeIter, isPrime

maxPrimes = 40
maxCoefProd = 41

# As the quadratic must produce a prime number when $n=0$, $b$ must be a prime.

# As the quadratic will never produce a prime when $n=b$, the quadratic will
# produce no more than $b$ consecutive primes, and so testing anything with
# $b<=41$ is pointless.

for b in dropwhile(lambda p: p<=41, primeIter(bound=1000)):
    for a in xrange(-999, 1000):
	if a == b+1 or a == b-1:
	    # The quadratic can be factored into (n ± b)(n ± 1) and so will
	    # produce no more than 2 consecutive primes.
	    continue
	if a*a >= 4*b:
	    bound = b
	    d = sqrt(a*a - 4*b)
	    x1 = (-a+d)/2
	    x2 = (-a-d)/2
	    if 0 < x1 < bound: bound = x1
	    if 0 < x2 < bound: bound = x2
	    if bound <= maxPrimes:
		continue
	n = 1
	while isPrime(n*n + a*n + b):
	   n += 1
	if n > maxPrimes:
	    maxPrimes = n
	    maxCoefProd = a*b
print maxCoefProd
