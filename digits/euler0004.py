#!/usr/bin/python
r"""Largest palindrome product

   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is $9009 = 91\times 99$.

   Find the largest palindrome made from the product of two 3-digit numbers."""

# Note: Assuming the largest palindrome is 6 digits long (which it is), it can
# be shown to be a multiple of 11, and thus at least one of its factors must be
# a multiple of 11.

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import generateAsc

__tags__ = ['digits', 'palindromic number', 'maximization']

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        return cmp(type(self), type(other)) \
            or cmp(other.x * other.y, self.x * self.y)

    def mknext(self):
        if self.x - 11 >= 100:
            yield Node(self.x-11, self.y)
        if self.x == 990 and self.y - 1 >= 100:
            yield Node(self.x, self.y-1)


def solve():
    for node in generateAsc([Node(990, 999)], Node.mknext):
        ns = str(node.x * node.y)
        if ns == ns[::-1]:
            return ns

if __name__ == '__main__':
    print solve()
