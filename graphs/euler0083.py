#!/usr/bin/python
"""Path sum: four ways

   NOTE: This problem is a significantly more challenging version of Problem
   81.

   In the 5 by 5 matrix below, the minimal path sum from the top left to the
   bottom right, by moving left, right, up, and down, is indicated in bold red
   and is equal to 2297.

       [131]    673    [234]   [103]   [ 18]
       [201]   [ 96]   [342]    965    [150]
        630     803     746    [422]   [111]
        537     699     497    [121]    956
        805     732     524    [ 37]   [331]

   Find the minimal path sum, in `matrix.txt` (right click and 'Save
   Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the
   top left to the bottom right by moving left, right, up, and down."""

from __future__ import with_statement
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib   import dijkstraLength

with open('../data/matrix.txt') as fp:
    matrix = map(lambda s: map(int, s.split(',')), fp)

width  = len(matrix[0])
height = len(matrix)

def neighbors(node):
    (y,x) = node
    if y > 0:
        yield (y-1, x)
    if x > 0:
        yield (y, x-1)
    if y+1 < height:
        yield (y+1, x)
    if x+1 < width:
        yield (y, x+1)

def length(_, node): return matrix[node[0]][node[1]]

print dijkstraLength((0,0), (height-1, width-1), neighbors, length) + matrix[0][0]
