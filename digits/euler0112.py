#!/usr/bin/python
"""Bouncy numbers

   Working from left-to-right if no digit is exceeded by the digit to its left
   it is called an increasing number; for example, 134468.

   Similarly if no digit is exceeded by the digit to its right it is called a
   decreasing number; for example, 66420.

   We shall call a positive integer that is neither increasing nor decreasing a
   "bouncy" number; for example, 155349.

   Clearly there cannot be any bouncy numbers below one-hundred, but just over
   half of the numbers below one-thousand (525) are bouncy.  In fact, the least
   number for which the proportion of bouncy numbers first reaches 50% is 538.

   Surprisingly, bouncy numbers become more and more common and by the time we
   reach 21780 the proportion of bouncy numbers is equal to 90%.

   Find the least number for which the proportion of bouncy numbers is exactly
   99%."""

import itertools

__tags__ = ['digits', 'bouncy number']

def solve():
    bounceless = 2178
    n = 21780
    while bounceless * 100 > n:
        n += 1
        nstr = [c for c,_ in itertools.groupby(str(n))]
        if len(nstr) == 1:
            bounceless += 1
        else:
            asc = nstr[0] < nstr[1]
            c = nstr[1]
            for d in nstr[2:]:
                if (asc and c > d) or (not asc and c < d):
                    break
                else:
                    c = d
            else:
                bounceless += 1
    return n

if __name__ == '__main__':
    print solve()
