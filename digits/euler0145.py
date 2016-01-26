#!/usr/bin/python
"""How many reversible numbers are there below one-billion?

   Some positive integers $n$ have the property that the sum [ $n$ +
   reverse($n$) ] consists entirely of odd (decimal) digits.  For instance, 36
   + 63 = 99 and 409 + 904 = 1313.  We will call such numbers *reversible*; so
   36, 63, 409, and 904 are reversible.  Leading zeroes are not allowed in
   either $n$ or reverse($n$).

   There are 120 reversible numbers below one-thousand.

   How many reversible numbers are there below one-billion ($10^9$)?"""

# Given a reversible number $n = a_1 a_2 ... a_i [m] b_i ... b_2 b_1$ (where
# $m$ is optional), observe the following:
#
# 1. As no single digit added to itself is odd, $i$ must be nonzero, and if $m$
#    is present, $a_i+b_i$ must be greater than 9 (i.e., "have carry").
#
# 2. If a pair $a_j+b_j$ has carry that, when carried, causes either $a_{j-1} +
#    b_{j-1}$ or $a_{j+1} + b_{j+1}$ to exceed 9 and thus gain carry, this will
#    result in the final sum containing a zero, and so $n$ is not reversible.
#    Thus, in order to determine the presence of carries, we need only look at
#    one $a_j+b_j$ at a time and not worry about "cascading" carries.
#
# 3. If some $a_j+b_j$ is even, then both $a_{j-1} + b_{j-1}$ and $a_{j+1} +
#    b_{j+1}$ (when they exist) must have carry.
#
# 4. If some $a_j+b_j$ has carry, then both $a_{j-1} + b_{j-1}$ and $a_{j+1} +
#    b_{j+1}$ (when they exist) must be even.
#
# 5. Due to the lack of carry to influence the ones-digit of the final sum,
#    $a_1 + b_1$ must be odd, and so $a_2 + b_2$ (when present) must not have
#    any carry.
#
# 6. Rules 3 and 4 together mean that, if two consecutive $a_j+b_j$ sums have
#    carry, then all digit sums must have carry, which contradicts rule 5.  In
#    particular, $m+m$ having carry (together with rule 1) would also cause all
#    digit sums to have carry, and so $m$ (when present) must be less than 5.
#
# 7. When $m$ is not present, repeatedly applying rules 3, 4, and 5 shows that
#    no digit pair can have carry, and so all even-length reversible numbers
#    are composed of digit pairs that add to odd numbers less than 10.
#
# 8. When $m$ is present, repeatedly applying rules 1, 3, 4, and 5 shows that
#    the sums $a_i+b_i$, $a_{i-2} + b_{i-2}$, etc. must all have carry & be odd
#    and that the sums $a_2+b_2$, $a_4+b_4$, etc. must not have carry & must be
#    even.  When $i$ is even, this leads to a contradiction, and so there are
#    no reversible numbers of length 1, 5, 9, 13, ..., 4k+1.

# Finally:
#  - There are 30 possible ordered pairs of digits that add to an odd number
#    less than 10.
#  - There are 20 possible ordered pairs of nonzero digits that add to an odd
#    number less than 10.
#  - There are 20 possible ordered pairs of (necessarily nonzero) digits that
#    add to an odd number greater than or equal to 10.
#  - There are 25 possible ordered pairs of digits that add to an even number
#    less than 10.
#  - There are 5 digits that add to a (necessarily even) number less than 10.

# And so...

__tags__ = ['digits']

qty = 0
for i in xrange(1,5):
    # Reversible numbers with 2*i digits:
    qty += 20 * 30**(i-1)
    # Reversible numbers with 2*i+1 digits:
    if i % 2:
        qty += 20**((i+1)//2) * 25**(i//2) * 5
print qty
