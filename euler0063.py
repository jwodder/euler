#!/usr/bin/python
"""Powerful digit counts

   The 5-digit number, $16807=7^5$, is also a fifth power.  Similarly, the
   9-digit number, $134217728=8^9$, is a ninth power.

   How many $n$-digit positive integers exist which are also an $n$th power?"""

# When $b$ has more than one digit, $b^n$ will always have more than $n$ digits.

# When $b$ has one digit, $b^n$ will have at most $n$ digits.  Once $b^n$ is
# less than $n$ digits long for some value of $n$, $b^{n+k}$ will continue to
# have fewer than $n+k$ digits for all $k$.

qty = 0
for base in range(1, 10):
    x = base
    i = 1
    while len(str(x)) == i:
	qty += 1
	x *= base
	i += 1
print qty
