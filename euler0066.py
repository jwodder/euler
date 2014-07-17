#!/usr/bin/python
r"""Diophantine equation

    Consider quadratic Diophantine equations of the form:</p>

    $$x^2 - Dy^2 = 1$$

    For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13\times
    180^2 = 1$.

    It can be assumed that there are no solutions in positive integers when $D$
    is square.

    By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain
    the following:

    $$3^2 - 2\times 2^2 = 1$$
    $$2^2 - 3\times 1^2 = 1$$
    $$[9]^2 - 5\times 4^2 = 1$$
    $$5^2 - 6\times 2^2 = 1$$
    $$8^2 - 7\times 3^2 = 1$$

    Hence, by considering minimal solutions in $x$ for $D\leq 7$, the largest
    $x$ is obtained when $D=5$.

    Find the value of $D\leq 1000$ in minimal solutions of $x$ for which the
    largest value of $x$ is obtained."""

from __future__ import division
from math       import sqrt, floor
from eulerlib   import reduceFrac

def sqrtConvergents(x):
    """Returns the successive convergents of the simple continued fraction
       representation of ``sqrt(x)`` as ``(numerator, denominator)`` pairs"""
    def continuedFrac(d):
	sqrtD = sqrt(d)
	P = 0
	Q = 1
	while True:
	    a = int(floor((P + sqrtD) / Q))
	    yield a
	    P = a * Q - P
	    Q = (d - P*P) // Q  # It can be shown that Q evenly divides d - P*P
    cfiter = continuedFrac(x)
    a0 = cfiter.next()
    a1 = cfiter.next()
    (pk, qk) = (a0, 1)
    (pk1, qk1) = (a0 * a1 + 1, a1)
    yield reduceFrac(pk, qk)
    yield reduceFrac(pk1, qk1)
    for a in cfiter:
	((pk,qk), (pk1, qk1)) = ((pk1, qk1), (a * pk1 + pk, a * qk1 + qk))
	yield reduceFrac(pk1, qk1)

squares = set(i*i for i in range(32))  # all perfect squares <= 1000

maxX = 0
maxD = 0
for d in xrange(2, 1001):
    if d in squares:
	continue
    for (x,y) in sqrtConvergents(d):
	if x*x - d * y * y == 1:
	    if x > maxX:
		maxX = x
		maxD = d
	    break
print maxD
