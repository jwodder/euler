#!/usr/bin/python
"""Largest exponential

   Comparing two numbers written in index form like $2^{11}$ and $3^7$ is not
   difficult, as any calculator would confirm that $2^{11} = 2048 < 3^7 =
   2187$.

   However, confirming that $632382^{518061} > 519432^{525806}$ would be much
   more difficult, as both numbers contain over three million digits.

   Using `base_exp.txt` (right click and 'Save Link/Target As...'), a 22K text
   file containing one thousand lines with a base/exponent pair on each line,
   determine which line number has the greatest numerical value.

   NOTE: The first two lines in the file represent the numbers in the example
   given above."""

from __future__ import with_statement
from math       import log

with open('data/base_exp.txt') as fp:
    nums = map(lambda s: map(float, s.split(',')), fp)
print max(xrange(len(nums)), key=lambda i: nums[i][1] * log(nums[i][0])) + 1
