#!/usr/bin/python
"""Squarefree Binomial Coefficients

   The binomial coefficients ${}^nC_k$ can be arranged in triangular form,
   Pascal's triangle, like this:

                     1
                   1   1
                 1   2   1
               1   3   3   1
             1   4   6   4   1
           1   5  10  10   5   1
         1   6  15  20  15   6   1
       1   7  21  35  35  21   7   1
                .........

   It can be seen that the first eight rows of Pascal's triangle contain twelve
   distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

   A positive integer $n$ is called squarefree if no square of a prime divides
   $n$.  Of the twelve distinct numbers in the first eight rows of Pascal's
   triangle, all except 4 and 20 are squarefree.  The sum of the distinct
   squarefree numbers in the first eight rows is 105.

   Find the sum of the distinct squarefree numbers in the first 51 rows of
   Pascal's triangle."""

from itertools import imap
from operator  import add
import sys; sys.path.insert(1, sys.path[0] + '/..')
from eulerlib.oldprimes import factor

numbers = set()
row = [1]

for i in xrange(51):
    for n in row:
        if all(k < 2 for _,k in factor(n)):
            numbers.add(n)
    row2 = list(imap(add, row, [0] + row))
    if i % 2 == 1:
        row2.append(row[-1] * 2)
    row = row2

print sum(numbers)
