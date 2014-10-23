#!/usr/bin/python
"""Cubic permutations

   The cube, 41063625 ($345^3$), can be permuted to produce two other cubes:
   56623104 ($384^3$) and 66430125 ($405^3$).  In fact, 41063625 is the
   smallest cube which has exactly three permutations of its digits which are
   also cube.

   Find the smallest cube for which exactly five permutations of its digits are
   cube."""

i = 1
cubeQtys = {}
cubelen = 1
while True:
    cubestr = ''.join(sorted(str(i**3))).lstrip('0')
    if len(cubestr) > cubelen:
	try:
	    match = min(j for q,j in cubeQtys.values() if q == 5)
	except ValueError:  # empty list
	    cubelen = len(cubestr)
	    cubeQtys = {}
	else:
	    print match**3
	    break
    cubeQtys.setdefault(cubestr, [0,i])[0] += 1
    i += 1
