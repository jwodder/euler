#!/usr/bin/python
"""Pandigital prime sets

   Using all of the digits 1 through 9 and concatenating them freely to form
   decimal integers, different sets can be formed.  Interestingly with the set
   {2,5,47,89,631}, all of the elements belonging to it are prime.

   How many distinct sets containing each of the digits one through nine
   exactly once contain only prime elements?"""

from itertools import ifilter, permutations, imap
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib  import sieve, isPrime, subsets

__tags__ = ['prime numbers', 'digits', 'permutation', 'digit permutation',
            'partitions of labeled elements into unlabeled bins']

def primeSets(digits):
    if len(digits) == 0:
        return 1
    else:
        accum = 0
        d = min(digits)
        igits = digits - {d}
        for ds in subsets(igits):
            if len(ds) == 8:
                continue
            arrangements = sum(isPrime(int(''.join(p)))
                               for p in permutations(ds+(d,)))
            if arrangements != 0:
                accum += arrangements * primeSets(igits.difference(ds))
        return accum

def solve():
    sieve(10**8)  # A 9-pandigital cannot be prime.
    return primeSets(set("123456789"))

if __name__ == '__main__':
    print solve()
