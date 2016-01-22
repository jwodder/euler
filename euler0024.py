#!/usr/bin/python
"""Lexicographic permutations

   A permutation is an ordered arrangement of objects.  For example, 3124 is
   one possible permutation of the digits 1, 2, 3 and 4.  If all of the
   permutations are listed numerically or alphabetically, we call it
   lexicographic order.  The lexicographic permutations of 0, 1 and 2 are:

       012   021   102   120   201   210

   What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
   5, 6, 7, 8 and 9?"""

__tags__ = ['digits', 'digit permutation', 'lexicographic order',
            'lexicographic permutations']

lehmer = 999999
degree = 10

def solve():
    mapping = []
    for i in range(1, degree+1):
        c = lehmer % i
        for (j,y) in enumerate(mapping):
            if y >= c:
                mapping[j] += 1
        mapping.insert(0,c)
        lehmer //= i
    return ''.join(str(c) for c in mapping)

if __name__ == '__main__':
    print solve()
