#!/usr/bin/python
r"""Digit fifth powers

    Surprisingly there are only three numbers that can be written as the sum of
    fourth powers of their digits:

    \begin{eqnarray*}
    1634 & = & 1^4 + 6^4 + 3^4 + 4^4 \\
    8208 & = & 8^4 + 2^4 + 0^4 + 8^4 \\
    9474 & = & 9^4 + 4^4 + 7^4 + 4^4
    \end{eqnarray*}

    As $1 = 1^4$ is not a sum it is not included.

    The sum of these numbers is $1634 + 8208 + 9474 = 19316$.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits."""

from itertools import combinations_with_replacement  # requires Python v.2.7+

maxDigits = 6
digits = [(i**5, str(i)) for i in range(10)]
accum = 0
for ndigs in combinations_with_replacement(digits, maxDigits):
    digPowers, digChars = zip(*ndigs)
    n = sum(digPowers)
    if n <= 1: continue
    if ''.join(sorted(str(n))).lstrip('0') == ''.join(digChars).lstrip('0'):
	accum += n
print accum
