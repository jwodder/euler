#!/usr/bin/python
"""Counting block combinations I

   A row measuring seven units in length has red blocks with a minimum length
   of three units placed on it, such that any two red blocks (which are allowed
   to be different lengths) are separated by at least one black square.  There
   are exactly seventeen ways of doing this.

       # # # # # # #    RRR # # # #    # RRR # # #

       # # RRR # #      # # # RRR #    # # # # RRR

       RRR # RRR        RRRR # # #     # RRRR # #

       # # RRRR #       # # # RRRR     RRRRR # #

       # RRRRR #        # # RRRRR      RRRRRR #

       # RRRRRR         RRRRRRR

   How many ways can a row measuring fifty units in length be filled?

   NOTE: Although the example above does not lend itself to the possibility, in
   general it is permitted to mix block sizes.  For example, on a row measuring
   eight units in length you could use red (3), black (1), and red (4)."""

placements = []
for n in xrange(51):
    if n < 3:
        placements.append(1)
    else:
        placements.append(placements[-1] + sum(placements[i-bool(i)]
                                               for i in xrange(n-2)))
print placements[50]
