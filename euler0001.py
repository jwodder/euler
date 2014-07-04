#!/usr/bin/python
n = 1000

def sum_of_mul(a,n):
    m = (n-1) // a
    return a * m * (m+1) // 2

print sum_of_mul(3,n) + sum_of_mul(5,n) - sum_of_mul(15,n)
