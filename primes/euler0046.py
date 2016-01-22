#!/usr/bin/python
r"""Goldbach's other conjecture

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    \begin{eqnarray*}
     9 & = & 7 + 2\times 1^2 \\
    15 & = & 7 + 2\times 2^2 \\
    21 & = & 3 + 2\times 3^2 \\
    25 & = & 7 + 2\times 3^2 \\
    27 & = & 19 + 2\times 2^2 \\
    33 & = & 31 + 2\times 1^2
    \end{eqnarray*}

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?"""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib import allprimes, generateAsc

__tags__ = ['prime numbers']

class Node(object):
    def __init__(self, prime, n=None):
        self.prime = prime
        self.n = n
        if self.n is None:
            self.val = next(self.prime)
        else:
            self.val = self.prime + 2 * self.n * self.n

    def next(self):
        if self.n is None:
            yield Node(self.prime)
            self.prime = self.val
            self.n = 0
        yield Node(self.prime, self.n+1)

    def __cmp__(self, other):
        return cmp(type(self), type(other)) or cmp(self.val, other.val)


def solve():
    piter = allprimes()
    next(piter)
    i = 3
    for node in generateAsc([Node(piter)], Node.next):
        if node.val > i:
            return i
        elif node.val == i:
            i += 2

if __name__ == '__main__':
    print solve()
