#!/usr/bin/python
"""Power digit sum

   $2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.

   What is the sum of the digits of the number $2^{1000}$?"""

__tags__ = ['digits', 'sum of digits']

def solve():
    return sum(int(c) for c in str(1 << 1000))

if __name__ == '__main__':
    print solve()
