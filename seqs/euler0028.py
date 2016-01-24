#!/usr/bin/python
"""Number spiral diagonals

   Starting with the number 1 and moving to the right in a clockwise direction
   a 5 by 5 spiral is formed as follows:

       [21] 22  23  24 [25]
        20 [ 7]  8 [ 9] 10
        19   6 [ 1]  2  11
        18 [ 5]  4 [ 3] 12
       [17] 16  15  14 [13]

   It can be verified that the sum of the numbers on the diagonals is 101.

   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
   formed in the same way?"""

# The diagonals are as follows:
#
#     1, 3, 13, 31, ..., 4n^2 - 2n + 1
#     1, 5, 17, 37, ..., 4n^2 + 1
#     1, 7, 21, 43, ..., 4n^2 + 2n + 1
#     1, 9, 25, 49, ..., 4n^2 + 4n + 1
#
# The sum of the corners at a distance $n>0$ from the center is thus $16n^2 +
# 4n + 4$, and so the sum of all corners at distance at most $n$ is:
#
#         1 + \sum_{i=1}^n 16i^2 + 4i + 4
#       = 1 + 16(\sum_{i=1}^n i^2) + 4(\sum_{i=1}^n i) + 4n
#       = 1 + 16n(n+1)(2n+1)/6 + 4n(n+1)/2 + 4n
#       = (16n^3 + 30n^2 + 26n + 3)/3

__tags__ = ['integer sequences', 'number spiral']

def solve():
    n = 500
    return 1 + n*(26 + n*(30 + n*16))//3

if __name__ == '__main__':
    print solve()
