#!/usr/bin/python
r"""(prime-k) factorial

    For a prime $p$ let $S(p) = (\sum(p-k)!) \bmod(p)$ for $1\leq k\leq 5$.

    For example, if $p=7$,

    $(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! =
    720+120+24+6+2 = 872$.

    As $872 \bmod(7) = 4$, $S(7) = 4$.

    It can be verified that $\sum S(p) = 480$ for $5\leq p < 100$.

    Find $\sum S(p)$ for $5\leq p < 10^8$."""

import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import primeIter, modInverse

# By Wilson's theorem, $(p-1)!\equiv -1\pmod{p}$.  Therefore (denoting the
# multiplicative inverse of $n$ _modulo_ $p$ as $n'$):
#
#    \sum_{k=1}^5 (p-k)!
#        \equiv (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)!
#        \equiv -1 + (-1)(p-1)' + (-1)(p-1)'(p-2)' + (-1)(p-1)'(p-2)'(p-3)'
#                  + (-1)(p-1)'(p-2)'(p-3)'(p-4)'
#        \equiv -1 + 1 + (-2)' + (-2)'(-3)' + (-2)'(-3)'(-4)'
#        \equiv (-2)' + (-2)'(-3)' + (-2)'(-3)'(-4)'

def S(p):
    inv2 = modInverse(-2, p)
    inv3 = modInverse(-3, p)
    inv4 = modInverse(-4, p)
    return (inv2 * (1 + inv3 * (1 + inv4))) % p

piter = primeIter(bound=10**8)
piter.next()
piter.next()
print sum(S(p) for p in piter)
