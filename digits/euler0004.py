#!/usr/bin/python
"""Largest palindrome product

   A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is $9009 = 91\times 99$.

   Find the largest palindrome made from the product of two 3-digit numbers."""

# Note: Assuming the largest palindrome is 6 digits long (which it is), it can
# be shown to be a multiple of 11, and thus at least one of its factors must be
# a multiple of 11.

from bisect import bisect_left

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        return cmp(type(self), type(other)) \
            or cmp(other.x * other.y, self.x * self.y)


def insert_uniq(queue, x):
    i = bisect_left(queue, x)
    if not (i < len(queue) and queue[i] == x):
        queue.insert(i,x)

nextHeap = [Node(990, 999)]
while True:
    node = nextHeap.pop(0)
    if node.x < 100 or node.y < 100: continue
    ns = str(node.x * node.y)
    if ns == ns[::-1]:
        print ns
        break
    insert_uniq(nextHeap, Node(node.x - 11, node.y))
    insert_uniq(nextHeap, Node(node.x, node.y - 1))
