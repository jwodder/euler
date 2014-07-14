"""In the 5 by 5 matrix below, the minimal path sum from the top left to the
   bottom right, by **only moving to the right and down**, is indicated in bold
   red and is equal to 2427.

       [131]    673     234     103      18
       [201]   [ 96]   [342]    965     150
        630     803    [746]   [422]    111
        537     699     497    [121]    956
        805     732     524    [ 37]   [331]

   Find the minimal path sum, in `matrix.txt` (right click and 'Save
   Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the
   top left to the bottom right by only moving right and down."""

from __future__ import with_statement

with open('data/matrix.txt') as fp:
    matrix = map(lambda s: map(int, s.split(',')), fp)

width  = len(matrix[0])
height = len(matrix)
destination = (height-1, width-1)

distances = [[None] * width for _ in range(height)]
distances[0][0] = matrix[0][0]
unvisited = set((y,x) for y in range(height) for x in range(width))
current = (0,0)

def neighbors(node):
    (y,x) = node
    if y+1 < height:
	yield (y+1, x)
    if x+1 < width:
	yield (y, x+1)

def nodeDist(node): return distances[node[0]][node[1]]

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
