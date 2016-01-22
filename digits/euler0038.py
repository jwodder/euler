#!/usr/bin/python
r"""Pandigital multiples

    Take the number 192 and multiply it by each of 1, 2, and 3:

    $$192\times 1 = 192$$
    $$192\times 2 = 384$$
    $$192\times 3 = 576$$

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and $(1,2,3)$

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and $(1,2,3,4,5)$.

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with $(1,2,\cdots,n)$ where $n>1?$"""

from itertools import permutations

__tags__ = ['digits', 'pandigital', 'maximization']

def initials(n):
    """Returns all `n`-digit integers where the first digit is 9, no digit is
       repeated, and 0 does not appear"""
    if n < 1: return []
    else: return [int('9' + ''.join(x)) for x in permutations('12345678', n-1)]

def solve():
    maxPD = '000000000'
    for n in range(2,10):
        for coef in initials(10//n - 1):
            product = ''.join(str(coef*i) for i in range(1,n+1))
            if ''.join(sorted(product)) == '123456789' and product > maxPD:
                maxPD = product
    return maxPD

if __name__ == '__main__':
    print solve()
