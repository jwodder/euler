#!/usr/bin/python
"""Path sum: three ways

   NOTE: This problem is a more challenging version of Problem 81.

   The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
   the left column and finishing in any cell in the right column, and only
   moving up, down, and right, is indicated in red and bold; the sum is equal
   to 994.

        131     673    [234]   [103]   [ 18]
       [201]   [ 96]   [342]    965     150 
        630     803     746     422     111 
        537     699     497     121     956
        805     732     524      37     331 

   Find the minimal path sum, in `matrix.txt` (right click and 'Save
   Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the
   left column to the right column."""

from __future__ import with_statement

with open('data/matrix.txt') as fp:
    matrix = map(lambda s: map(int, s.split(',')), fp)

width  = len(matrix[0])
height = len(matrix)

# Pseudo-points with value 0 to the left of the left column and right of the
# right column:
start = (-1, -1)
destination = (height, width)
matrix.append([0] * (width+1))

distances = [[None] * (width+1) for _ in range(height+1)]
unvisited = set((y,x) for y in range(height) for x in range(width))
unvisited.add(start)
unvisited.add(destination)
current = start

def neighbors(node):
    if node == start:
	for y in xrange(height):
	    yield (y,0)
    elif node != destination:
	(y,x) = node
	if y > 0:
	    yield (y-1, x)
	if y+1 < height:
	    yield (y+1, x)
	if x+1 < width:
	    yield (y, x+1)
	if x == width-1:
	    yield destination

def nodeDist(node): return 0 if node == start else distances[node[0]][node[1]]

while True:
    for (y,x) in neighbors(current):
	if (y,x) in unvisited:
	    newdist = nodeDist(current) + matrix[y][x]
	    olddist = nodeDist((y,x))
	    if olddist is None or olddist > newdist:
		distances[y][x] = newdist
    unvisited.remove(current)
    if destination not in unvisited:
	print nodeDist(destination)
	break
    visitable = [n for n in unvisited if nodeDist(n) is not None]
    if visitable:
	current = min(visitable, key=nodeDist)
    else:
	print "No route to endpoint"
	break