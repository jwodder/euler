#!/usr/bin/python
"""Licence plates

   Oregon licence plates consist of three letters followed by a three digit
   number (each digit can be from [0..9]).

   While driving to work Seth plays the following game:

   Whenever the numbers of two licence plates seen on his trip add to 1000
   that's a win.

   E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too. (as long as
   he sees them in the same trip).

   Find the expected number of plates he needs to see for a win.

   Give your answer rounded to 8 decimal places behind the decimal point.

   **Note:** We assume that each licence plate seen is equally likely to have
   any three digit number on it."""

# Having seen $n$ different nonzero license plates that do not give a win, let
# $E_n$ be the expected number of further license plates that need to be seen
# in order to win when 500 has not been seen yet, and let $E_n'$ be the
# expected number when 500 has been seen.  Then:
#
#    E_n = 1 * (n/1000)                          # next plate lets us win
#        + (1+E_n) (n/1000)                      # next plate is already seen
#        + (1+E_n) (1/1000)                      # next plate is 0
#        + (1 + E_{n+1}') (1/1000)               # next plate is 500
#        + (1 + E_{n+1}) ((1000 - 2n - 2)/1000)  # next plate is nonzero new
#
#    E_n' = 1 * (n/1000)                         # next plate lets us win
#         + (1 + E_n') ((n-1)/1000)              # next plate is already seen
#                                                #  (excluding 500, which wins)
#         + (1 + E_n') (1/1000)                  # next plate is 0
#         + (1 + E_{n+1}') ((1000 - 2n)/1000)    # next plate is nonzero new
#
# These simplify to:
#
#    E_n  = (1000 + E_{n+1}' + E_{n+1}(1000 - 2n - 2)) / (1000 - n - 1)
#    E_n' = (1000 + E_{n+1}'(1000 - 2n)) / (1000 - n)
#
# from which we can determine the "base cases":
#
#    E_{500}' = 2
#    E_{499}  = 501 / 250
#
# Now find $E_0$.

from fractions import Fraction
from eulerlib  import sprintFFraction

E1prime = Fraction(1000 + 2 * (1000 - 2*499), 1000 - 499)
E = Fraction(501, 250)

for n in xrange(498, -1, -1):
    (E, E1prime) = ((1000 + E1prime + E * (1000 - 2*n - 2)) / (1000 - n - 1),
                    (1000 + E1prime * (1000 - 2*n)) / (1000 - n))

print sprintFFraction(8, E.numerator, E.denominator)
