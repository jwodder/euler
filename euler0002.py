#!/usr/bin/python
n = 4000000
(a,b) = (1,2)
accum = 0
while b <= n:
    if b % 2 == 0: accum += b
    (a,b) = (b, a+b)
print accum
