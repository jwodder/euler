#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Disc game prize fund

   A bag contains one red disc and one blue disc.  In a game of chance a player
   takes a disc at random and its colour is noted.  After each turn the disc is
   returned to the bag, an extra red disc is added, and another disc is taken
   at random.

   The player pays £1 to play and wins if they have taken more blue discs than
   red discs at the end of the game.

   If the game is played for four turns, the probability of a player winning is
   exactly 11/120, and so the maximum prize fund the banker should allocate for
   winning in this game would be £10 before they would expect to incur a loss.
   Note that any payout will be a whole number of pounds and also includes the
   original £1 paid to play the game, so in the example given the player
   actually wins £9.

   Find the maximum prize fund that should be allocated to a single game in
   which fifteen turns are played."""

# Requires Python v.2.6+
from fractions import Fraction
from itertools import combinations
from eulerlib  import product

turns = 15
allRed = Fraction(1, turns+1)

probability = Fraction(0)
for blueQty in range(turns//2 + 1, turns+1):
    for combo in combinations(range(1, turns+1), blueQty):
	probability += allRed / product(combo)
print int((1 - probability) / probability) + 1
