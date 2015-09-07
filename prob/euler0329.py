#!/usr/bin/python
"""Prime Frog

   Susan has a prime frog.

   Her frog is jumping around over 500 squares numbered 1 to 500.  He can only
   jump one square to the left or to the right, with equal probability, and he
   cannot jump outside the range $[1;500]$.

   (if it lands at either end, it automatically jumps to the only available
   square on the next move.)

   When he is on a square with a prime number on it, he croaks 'P' (PRIME) with
   probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before jumping
   to the next square.

   When he is on a square with a number on it that is not a prime he croaks 'P'
   with probability 1/3 or 'N' with probability 2/3 just before jumping to the
   next square.

   Given that the frog's starting position is random with the same probability
   for every square, and given that she listens to his first 15 croaks, what is
   the probability that she hears the sequence PPPPNNPPPNPPNPN?

   Give your answer as a fraction $p/q$ in reduced form."""

from collections import defaultdict
from fractions   import Fraction
from eulerlib    import sieve, isPrime

sieve(500)

def jump(state):
    # state: mapping from square to list of probabilities
    state2 = defaultdict(list)
    for sq, frogs in state.iteritems():
        if sq == 1:
            state2[2].extend(frogs*2)
        elif sq == 500:
            state2[499].extend(frogs*2)
        else:
            state2[sq-1].extend(frogs)
            state2[sq+1].extend(frogs)
    return state2

accum = Fraction(0)
for start in xrange(1, 501):
    state = {start: [1]}
    for primal in [c == 'P' for c in 'PPPPNNPPPNPPNPN']:
        for sq in state.keys():
            coef = Fraction(2 if primal == bool(isPrime(sq)) else 1, 3)
            state[sq] = [p * coef for p in state[sq]]
        state = jump(state)
    accum += sum(p for frogs in state.itervalues() for p in frogs) / \
             sum(map(len, state.itervalues()))
print accum / 500
