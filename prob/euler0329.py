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

from   fractions import Fraction
import operator
from   eulerlib  import sieve, isPrime

__tags__ = ['prime numbers', 'probability']

def jump(state):
    state2 = map(operator.add, [p/2 for p in state[1:]] + [0],
                               [0] + [p/2 for p in state[:-1]])
    state2[1] += state[0]/2
    state2[-2] += state[-1]/2
    return state2

def solve():
    sieve(500)
    P = [Fraction(2 if isPrime(i) else 1, 3) for i in xrange(1, 501)]
    N = [1 - p for p in P]
    state = [Fraction(1, 500)] * 500
    for primal in [P if c == 'P' else N for c in 'PPPPNNPPPNPPNPN']:
        state = jump(map(operator.mul, state, primal))
    return sum(state)

if __name__ == '__main__':
    print solve()
