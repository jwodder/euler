#!/usr/bin/python
r"""A Modified Collatz sequence

    A modified Collatz sequence of integers is obtained from a starting value
    $a_1$ in the following way:

    $a_{n+1}$ = $a_n/3$ if $a_n$ is divisible by 3.  We shall denote this as a
    large downward step, "D".

    $a_{n+1}$ = $(4a_n + 2)/3$ if $a_n$ divided by 3 gives a remainder of 1.
    We shall denote this as an upward step, "U".

    $a_{n+1}$ = $(2a_n - 1)/3$ if $a_n$ divided by 3 gives a remainder of 2.
    We shall denote this as a small downward step, "d".

    The sequence terminates when some $a_n = 1$.

    Given any integer, we can list out the sequence of steps.

    For instance if $a_1=231$, then the sequence $\{a_n} =
    \{231,77,51,17,11,7,10,14,9,3,1\}$ corresponds to the steps "DdDddUUdDD".

    Of course, there are other sequences that begin with that same sequence
    "DdDddUUdDD....".

    For instance, if $a_1=1004064$, then the sequence is
    DdDddUUdDDDdUDUUUdDdUUDDDUdDD.

    In fact, 1004064 is the smallest possible $a_1 > 10^6$ that begins with the
    sequence DdDddUUdDD.

    What is the smallest $a_1 > 10^{15}$ that begins with the sequence
    "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?"""

from fractions           import Fraction
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib            import modInverse
from eulerlib.polynomial import Polynomial

__tags__ = ['integer sequences', 'Collatz conjecture', 'Collatz variants',
            'minimization', 'iterated functions']

def solve():
    reverseOps = {
        'D': Polynomial(0,3),
        'U': Polynomial(Fraction(-1,2), Fraction(3,4)),
        'd': Polynomial(Fraction(1,2), Fraction(3,2)),
    }

    seq = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
    poly = reduce(lambda accum, op: reverseOps[op](accum), seq[::-1],
                  Polynomial.X)

    # The resulting polynomial is of the form $(a/b)x + c/b$.  (Note that the
    # denominators are equal.)  We then need to find the smallest $z > 10^{15}$
    # that is in the range of this polynomial, i.e., the smallest $z > 10^{15}$
    # such that its preimage $(z - c/b)(b/a) = (zb - c)/a$ is an integer, i.e.,
    # such that $a$ divides $zb - c$, i.e., such that $z$ is congruent to
    # $cb^{-1}$ _modulo_ $a$.

    a = poly.coef(1).numerator
    b = poly.coef(1).denominator
    c = poly.coef(0).numerator

    rem = (c * modInverse(b,a)) % a
    return (10**15 // a + (10**15 % a > rem)) * a + rem

if __name__ == '__main__':
    print solve()
