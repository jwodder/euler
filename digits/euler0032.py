#!/usr/bin/python
r"""Pandigital products

    We shall say that an $n$-digit number is pandigital if it makes use of all
    the digits 1 to $n$ exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, $39\times 186 = 7254$,
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum."""

from itertools import permutations  # requires Python v.2.6+

def fromDigits(xs): return int(''.join(xs))

products = set()
for pandigital in permutations('123456789'):
    (a,b,c) = map(fromDigits, (pandigital[:1], pandigital[1:5], pandigital[5:]))
    if a * b == c:
        products.add(c)
    (a,b,c) = map(fromDigits, (pandigital[:2], pandigital[2:5], pandigital[5:]))
    if a * b == c:
        products.add(c)
print sum(products)
