#!/usr/bin/python
"""Using up to one million tiles how many different "hollow" square laminae can
   be formed?

   We shall define a square lamina to be a square outline with a square "hole"
   so that the shape possesses vertical and horizontal symmetry.  For example,
   using exactly thirty-two square tiles we can form two different square
   laminae:

                             ######  #########
                             ######  #       #
                             ##  ##  #       #
                             ##  ##  #       #
                             ######  #       #
                             ######  #       #
                                     #       #
                                     #       #
                                     #########

   With one-hundred tiles, and not necessarily using all of the tiles at one
   time, it is possible to form forty-one different square laminae.

   Using up to one million tiles how many different square laminae can be
   formed?"""

maxTiles = 1000000

def countParity(start):
    used = start*4 + (start-2) * 4
    outer = start
    qty = 0
    for i in xrange(start, maxTiles//4 + 1, 2):
        used -= (i-2)*4
        while used + (outer+2)*4 <= maxTiles:
            outer += 2
            used += outer*4
        qty += (outer - i) // 2 + 1
    return qty

print countParity(2) + countParity(3)
