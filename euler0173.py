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

# The number of laminae with an inner hole of side length $s$ that can be
# formed from at most 1e6 tiles is $(S-s)/2$ where $S$ is the largest integer
# of the same parity as $s$ such that $S^2 - s^2 \leq 1e6$, i.e., `S =
# floor(sqrt(1e6 + s*s))`, possibly minus 1 (difference eliminated by rounding
# down when dividing by 2).

import math

__tags__ = ['integer sequences', 'arithmetic sequence', 'partial sums',
            'integer partition']

maxTiles = 1000000

def intSqrt(x):
    # faster than the one in eulerlib, and just as accurate
    return int(math.floor(math.sqrt(x)))

def solve():
    return sum((intSqrt(maxTiles + s*s) - s)//2 for s in xrange(1, maxTiles//4))

if __name__ == '__main__':
    print solve()
