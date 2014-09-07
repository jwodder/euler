#!/usr/bin/python
r"""Digit canceling fractions

    The fraction $\frac{49}{98}$ is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    $\frac{49}{98} = \frac{4}{8}$, which is correct, is obtained by cancelling
    the 9s.

    We shall consider fractions like, $\frac{30}{50} = \frac{3}{5}$, to be
    trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator."""

from eulerlib import product, gcd

fractions = []

# ab/bc = a/c
#   (10a + b)c = (10b + c)a
#   10ac + bc = 10ba + ca
#   9ac = b(10a - c)
for a in range(1, 10):
    for b in range(1, 10):
	ab = a * 10 + b
	for c in range(1, 10):
	    bc = 10 * b + c
	    if ab >= bc: continue
	    if ab * c == bc * a:
		fractions.append((a,c))

# ab/cb = a/c
for a in range(1, 10):
    for b in range(1, 10):
	ab = a * 10 + b
	for c in range(1, 10):
	    cb = 10 * c + b
	    if ab >= cb: continue
	    if ab * c == cb * a:
		fractions.append((a,c))

# ab/ac = b/c
for a in range(1, 10):
    for b in range(1, 10):
	ab = a * 10 + b
	for c in range(b+1, 10):
	    ac = 10 * a + c
	    #if ab >= ac: continue
	    if ab * c == ac * b:
		fractions.append((b,c))

# ab/ca = b/c
for a in range(1, 10):
    for b in range(1, 10):
	ab = a * 10 + b
	for c in range(1, 10):
	    ca = 10 * c + a
	    if ab >= ca: continue
	    if ab * c == ca * b:
		fractions.append((b,c))

(nums, denoms) = zip(*fractions)
num = product(nums)
denom = product(denoms)
print denom // gcd(num, denom)
