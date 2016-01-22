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

from itertools import permutations

__tags__ = ['digits', 'pandigital']

def fromDigits(xs):
    return int(''.join(xs))

def solve():
    products = set()
    for pan in permutations('123456789'):
        (a,b,c) = map(fromDigits, (pan[:1], pan[1:5], pan[5:]))
        if a * b == c:
            products.add(c)
        (a,b,c) = map(fromDigits, (pan[:2], pan[2:5], pan[5:]))
        if a * b == c:
            products.add(c)
    return sum(products)

if __name__ == '__main__':
    print solve()
