#!/usr/bin/python
r"""Lattice paths

    Starting in the top left corner of a $2\times 2$ grid, and only being able
    to move to the right and down, there are exactly 6 routes to the bottom
    right corner.

    How many such routes are there through a $20\times 20$ grid?"""

# Answer: \binom{40}{20} ("40 choose 20") because each route is uniquely
# identified by which 20 of the 40 steps you use to move down (or,
# equivalently, right)

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import nCr
print nCr(40, 20)
