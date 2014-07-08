r"""By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

             _3_
           _7_  4
          2  _4_  6
        8   5  _9_  3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in `triangle.txt` (right click
    and 'Save Link/Target As...'), a 15K text file containing a triangle with
    one-hundred rows.

    **NOTE:** This is a much more difficult version of Problem 18.  It is not
    possible to try every route to solve this problem, as there are $2^{99}$
    altogether! If you could check one trillion ($10^12$) routes every second
    it would take over twenty billion years to check them all.  There is an
    efficient algorithm to solve it. ;o)"""

from __future__ import with_statement

with open('data/triangle.txt') as fp:
    triangle = map(lambda s: map(int, s.split()), fp)

accums = triangle[0]
for row in triangle[1:]:
    accums = map(lambda a,b,c: a + max(b,c), row, accums+[0], [0]+accums)
print max(accums)
