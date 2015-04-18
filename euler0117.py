#!/usr/bin/python
"""Red, green, and blue tiles

   Using a combination of black square tiles and oblong tiles chosen from: red
   tiles measuring two units, green tiles measuring three units, and blue tiles
   measuring four units, it is possible to tile a row measuring five units in
   length in exactly fifteen different ways.

       # # # # #    RR # # #    # RR # #    # # RR #

       # # # RR     RR RR #     RR # RR     # RR RR

       GGG # #      # GGG #     # # GGG     RR GGG

       GGG RR       BBBB #      # BBBB

   How many ways can a row measuring fifty units in length be tiled?

   NOTE: This is related to Problem 116."""

cache = [None] * 51

def repl(i):
    if cache[i] is None:
        cache[i] = 1 + sum(repl(j) for sz in [2,3,4] for j in xrange(i-sz+1))
    return cache[i]

print repl(50)
