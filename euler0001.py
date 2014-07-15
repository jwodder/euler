#!/usr/bin/python
"""Multiples of 3 and 5

   If we list all the natural numbers below 10 that are multiples of 3 or 5, we
   get 3, 5, 6 and 9.  The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000."""

n = 1000

def sum_of_mul(a,n):
    m = (n-1) // a
    return a * m * (m+1) // 2

print sum_of_mul(3,n) + sum_of_mul(5,n) - sum_of_mul(15,n)
