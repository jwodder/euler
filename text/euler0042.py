#!/usr/bin/python
r"""Coded triangle numbers

    The $n$th term of the sequence of triangle numbers is given by, $t_n =
    \frac{1}{2}n(n+1)$; so the first ten triangle numbers are:

    $$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \ldots$$

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.  For
    example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$.  If the
    word value is a triangle number then we shall call the word a triangle
    word.

    Using `words.txt` (right click and 'Save Link/Target As...'), a 16K text
    file containing nearly two-thousand common English words, how many are
    triangle words?"""

from __future__ import with_statement

with open('data/words.txt') as fp:
    words = fp.read().strip('"').split('","')

triangles = set([1, 3, 6, 10, 15]);
maxTri = 15
qty = 0
for word in words:
    val = sum(ord(c) - 64 for c in word)
    while val > maxTri:
	maxTri += len(triangles) + 1
	triangles.add(maxTri)
    if val in triangles:
	qty += 1
print qty
