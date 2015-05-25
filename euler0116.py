#!/usr/bin/python
"""Red, green or blue tiles

   A row of five black square tiles is to have a number of its tiles replaced
   with coloured oblong tiles chosen from red (length two), green (length
   three), or blue (length four).

   If red tiles are chosen there are exactly seven ways this can be done.

       RR # # #    # RR # #    # # RR #    # # # RR

       RR RR #     RR # RR     # RR RR

   If green tiles are chosen there are three ways.

       GGG # #     # GGG #     # # GGG

   And if blue tiles are chosen there are two ways.

       # BBBB      BBBB #

   Assuming that colours cannot be mixed there are $7 + 3 + 2 = 12$ ways of
   replacing the black tiles in a row measuring five units in length.

   How many different ways can the black tiles in a row measuring fifty units
   in length be replaced if colours cannot be mixed and at least one coloured
   tile must be used?

   NOTE: This is related to Problem 117."""

def replacements(n, size):
    repl = []
    for i in xrange(n+1):
        repl.append(1 + sum(repl[:max(i-size+1,0)]))
    return repl[-1] - 1

print replacements(50,2) + replacements(50,3) + replacements(50,4)
