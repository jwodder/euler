#!/usr/bin/python
r"""Odd period square roots

    All square roots are periodic when written as continued fractions and can
    be written in the form:

    $$\sqrt{N} = a_0 + \dfrac{1}{a_1 + \dfrac{1}{a_2 + \dfrac{1}{a_3 +
    \ldots}}}$$

    For example, let us consider $\sqrt{23}$:

    $$\sqrt{23} = 4 + \sqrt{23} - 4 = 4 + \dfrac{1}{\dfrac{1}{\sqrt{23}-4}} = 4
    + \dfrac{1}{1 + \dfrac{\sqrt{23}-3}{7}}$$

    If we continue we would get the following expansion:

    $$\sqrt{23} = 4 + \dfrac{1}{1 + \dfrac{1}{3 + \dfrac{1}{1 + \dfrac{1}{8 +
    \ldots}}}}$$

    The process can be summarised as follows:

    $a_0 = 4$, $\frac{1}{\sqrt{23}-4} = \frac{\sqrt{23}+4}{7} = 1 +
    \frac{\sqrt{23}-3}{7}$

    $a_1 = 1$, $\frac{7}{\sqrt{23}-3} = \frac{7(\sqrt{23}+3)}{14} = 3 +
    \frac{\sqrt{23}-3}{2}$

    $a_2 = 3$, $\frac{2}{\sqrt{23}-3} = \frac{2(\sqrt{23}+3)}{14} = 1 +
    \frac{\sqrt{23}-4}{7}$

    $a_3 = 1$, $\frac{7}{\sqrt{23}-4} = \frac{7(\sqrt{23}+4)}{7} = 8 +
    \sqrt{23}-4$

    $a_4 = 8$, $\frac{1}{\sqrt{23}-4} = \frac{\sqrt{23}+4}{7} = 1 +
    \frac{\sqrt{23}-3}{7}$

    $a_5 = 1$, $\frac{7}{\sqrt{23}-3} = \frac{7(\sqrt{23}+3)}{14} = 3 +
    \frac{\sqrt{23}-3}{2}$

    $a_6 = 3$, $\frac{2}{\sqrt{23}-3} = \frac{2(\sqrt{23}+3)}{14} = 1 +
    \frac{\sqrt{23}-4}{7}$

    $a_7 = 1$, $\frac{7}{\sqrt{23}-4} = \frac{7(\sqrt{23}+4)}{7} = 8 +
    \sqrt{23}-4$

    It can be seen that the sequence is repeating.  For conciseness, we use the
    notation $\sqrt{23} = [4;(1,3,1,8)]$, to indicate that the block
    $(1,3,1,8)$ repeats indefinitely.

    The first ten continued fraction representations of (irrational) square
    roots are:

        $\sqrt{2}=[1;(2)]$, period=1
        $\sqrt{3}=[1;(1,2)]$, period=2
        $\sqrt{5}=[2;(4)]$, period=1
        $\sqrt{6}=[2;(2,4)]$, period=2
        $\sqrt{7}=[2;(1,1,1,4)]$, period=4
        $\sqrt{8}=[2;(1,4)]$, period=2
        $\sqrt{10}=[3;(6)]$, period=1
        $\sqrt{11}=[3;(3,6)]$, period=2
        $\sqrt{12}=[3;(2,6)]$, period=2
        $\sqrt{13}=[3;(1,1,1,1,6)]$, period=5

    Exactly four continued fractions, for $N\leq 13$, have an odd period.

    How many continued fractions for $N\leq 10000$ have an odd period?"""

from __future__ import division
from math       import sqrt, floor, ceil

__tags__ = ['continued fractions', 'square root']

def sqrtCF_PQ(d):
    """Returns the P and Q values used in the calculation of the simple
       continued fraction representation of ``sqrt(d)``"""
    sqrtD = sqrt(d)
    P = 0
    Q = 1
    while True:
        yield (P,Q)
        a = int(floor((P + sqrtD) / Q))
        P = a * Q - P
        Q = (d - P*P) // Q  # It can be shown that Q evenly divides d - P*P

def solve():
    squares = set(i*i for i in xrange(1, int(ceil(sqrt(10000)))))
    qty = 0
    for n in xrange(2, 10000):
        if n in squares:
            continue
        pqs = sqrtCF_PQ(n)
        pqs.next()
        start = pqs.next()
        i = 1
        while start != pqs.next():
            i += 1
        if i % 2 == 1:
            qty += 1
    return qty

if __name__ == '__main__':
    print solve()
