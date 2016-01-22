#!/usr/bin/python
"""Anagramic squares

   By replacing each of the letters in the word CARE with 1, 2, 9, and 6
   respectively, we form a square number: $1296 = 36^2$.  What is remarkable is
   that, by using the same digital substitutions, the anagram, RACE, also forms
   a square number: $9216 = 96^2$.  We shall call CARE (and RACE) a square
   anagram word pair and specify further that leading zeroes are not permitted,
   neither may a different letter have the same digital value as another
   letter.

   Using `words.txt` (right click and 'Save Link/Target As...'), a 16K text
   file containing nearly two-thousand common English words, find all the
   square anagram word pairs (a palindromic word is NOT considered to be an
   anagram of itself).

   What is the largest square number formed by any member of such a pair?

   NOTE: All anagrams formed must be contained in the given text file."""

from collections import defaultdict
from itertools   import combinations, groupby, permutations
from string      import digits, maketrans
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib    import isPerfectSquare

__tags__ = ['digits', 'perfect square', 'permutation', 'digit permutation',
            'text']

def solve():
    with open('../data/words.txt') as fp:
        words = fp.read().strip('"').split('","')
    anagrams = defaultdict(list)
    for w in words:
        anagrams[''.join(sorted(w))].append(w)
    maxval = 0
    for (letters, vals) in anagrams.iteritems():
        letters = ''.join(c for c,_ in groupby(letters))
        for word1, word2 in combinations(vals, 2):
            for assignment in permutations(digits, len(letters)):
                tbl = maketrans(letters, ''.join(assignment))
                int1 = word1.translate(tbl)
                int2 = word2.translate(tbl)
                if int1[0] == '0' or int2[0] == '0':
                    continue
                int1 = int(int1)
                int2 = int(int2)
                if isPerfectSquare(int1) and isPerfectSquare(int2):
                    maxval = max(maxval, int1, int2)
    return maxval

if __name__ == '__main__':
    print solve()
