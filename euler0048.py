#!/usr/bin/python
"""Self powers

   The series, $1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317$.

   Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + ... +
   1000^{1000}$."""

__tags__ = ['digits', 'last n digits', 'integer sequences']

modulus = 10**10

def solve():
    accum = 0
    for i in xrange(1, 1001):
        accum = (accum + i**i) % modulus
    return accum

if __name__ == '__main__':
    print solve()
