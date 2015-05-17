#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Counting rectangles

   By counting carefully it can be seen that a rectangular grid measuring 3 by
   2 contains eighteen rectangles:

       ╔═╗─┬─┐    ╔═══╗─┐    ╔═════╗
       ║ ║ │ │    ║   ║ │    ║     ║
       ╚═╝─┼─┤    ╚═╤═╝─┤    ╚═╤═╤═╝
       │ │ │ │    │ │ │ │    │ │ │ │
       └─┴─┴─┘    └─┴─┴─┘    └─┴─┴─┘
          6          4          2

       ╔═╗─┬─┐    ╔═══╗─┐    ╔═════╗
       ║ ║ │ │    ║   ║ │    ║     ║
       ║ ╟─┼─┤    ║   ╟─┤    ║     ║
       ║ ║ │ │    ║   ║ │    ║     ║
       ╚═╝─┴─┘    ╚═══╝─┘    ╚═════╝
          3          2          1

   Although there exists no rectangular grid that contains exactly two million
   rectangles, find the area of the grid with the nearest solution."""

# In a rectangle of width $W$ and height $H$, the number of subrectangles of
# width $w$ and height $h$ is $(W-w+1)(H-h+1)$.  Thus, the total number of
# subrectangles is:
#
#      \sum_{w=1}^W \sum_{h=1}^H (W-w+1)(H-h+1)
#           = (\sum_{w=1}^W (W-w+1)) (\sum_{h=1}^H (H-h+1))
#           = (\sum_{w=1}^W w) (\sum_{h=1}^H h)
#           = ((W^2 + W) / 2) ((H^2 + H) / 2)
#           = WH(W+1)(H+1) / 4

from __future__ import division
from math       import sqrt, floor, ceil

n = 2000000
bestDelta = n
bestArea = 0

# For widths beyond 2000, the number of subrectangles is always considerably
# greater than two million.
for w in xrange(1, 2001):
    # For each W, the best H is the one that minimizes $|n - WH(W+1)(H+1)/4|$,
    # i.e., the closest integer to $\sqrt{4n/W/(W+1)}$.
    happrox = sqrt(4*n / w / (w+1))
    for h in (int(floor(happrox)), int(ceil(happrox))):
        rects = w * h * (w+1) * (h+1) // 4
        if abs(n - rects) < bestDelta:
            bestDelta = abs(n - rects)
            bestArea = w*h
print bestArea
