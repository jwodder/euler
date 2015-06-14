#!/usr/bin/python
"""Arithmetic expressions

   By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
   making use of the four arithmetic operations (+, -, *, /) and
   brackets/parentheses, it is possible to form different positive integer
   targets.

   For example,

       8 = (4 * (1 + 3)) / 2
       14 = 4 * (3 + 1 / 2)
       19 = 4 * (2 + 3) - 1
       36 = 3 * 4 * (2 + 1)

   Note that concatenations of the digits, like 12 + 34, are not allowed.

   Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
   target numbers of which 36 is the maximum, and each of the numbers 1 to 28
   can be obtained before encountering the first non-expressible number.

   Find the set of four distinct digits, $a<b<c<d$, for which the longest set
   of consecutive positive integers, 1 to $n$, can be obtained, giving your
   answer as a string: $abcd$."""

from   fractions import Fraction
import itertools
from   operator  import add, sub, mul, div

trees = [
    lambda op1, op2, op3: lambda a,b,c,d: op1(a, op2(b, op3(c, d))),
    lambda op1, op2, op3: lambda a,b,c,d: op1(a, op2(op3(b, c), d)),
    lambda op1, op2, op3: lambda a,b,c,d: op1(op2(a, op3(b, c)), d),
    lambda op1, op2, op3: lambda a,b,c,d: op1(op2(op3(a, b), c), d),
    lambda op1, op2, op3: lambda a,b,c,d: op1(op2(a, b), op3(c, d)),
]

formulae = [t(*ops) for ops in itertools.product((add, sub, mul, div), repeat=3)
                    for t in trees]

def consecExpr(vals):
    n = 0
    beyondN = set()
    for args in itertools.permutations(map(Fraction, vals)):
        for f in formulae:
            try:
                x = f(*args)
            except ZeroDivisionError:
                pass
            else:
                if x >= n:
                    beyondN.add(x)
                    while (n+1) in beyondN:
                        n += 1
                        beyondN.remove(n)
    return n

print ''.join(map(str, max(itertools.combinations((1,2,3,4,5,6,7,8,9), 4),
                           key=consecExpr)))
