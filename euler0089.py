#!/usr/bin/python
"""Roman numerals

   For a number written in Roman numerals to be considered valid there are
   basic rules which must be followed. Even though the rules allow some numbers
   to be expressed in more than one way there is always a "best" way of writing
   a particular number.

   For example, it would appear that there are at least six ways of writing the
   number sixteen:

       IIIIIIIIIIIIIIII
       VIIIIIIIIIII
       VVIIIIII
       XIIIIII
       VVVI
       XVI

   However, according to the rules only `XIIIIII` and `XVI` are valid, and the
   last example is considered to be the most efficient, as it uses the least
   number of numerals.

   The 11K text file, `roman.txt` (right click and 'Save Link/Target As...'),
   contains one thousand numbers written in valid, but not necessarily minimal,
   Roman numerals; see [About... Roman
   Numerals](https://projecteuler.net/about=roman_numerals) for the definitive
   rules for this problem.

   Find the number of characters saved by writing each of these in their
   minimal form.

   Note: You can assume that all the Roman numerals in the file contain no more
   than four consecutive identical units."""

from __future__ import with_statement

qty = 0
with open('data/roman.txt') as fp:
    for line in fp:
	line = line.strip()
	origLen = len(line)
	for i,v,x in ('IVX', 'XLC', 'CDM'):
	    line = line.replace(i * 5, v)
	    line = line.replace(v + i * 4, i + x)
	    line = line.replace(i * 4, i + v)
	    line = line.replace(i + v + i, v)
	    line = line.replace(v * 2, x)
	    line = line.replace(i + x + i, x)
	qty += origLen - len(line)
print qty
