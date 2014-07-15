#!/usr/bin/python
"""Even Fibonacci numbers

   Each new term in the Fibonacci sequence is generated by adding the previous
   two terms. By starting with 1 and 2, the first 10 terms will be:

   $$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \ldots$$

   By considering the terms in the Fibonacci sequence whose values do not
   exceed four million, find the sum of the even-valued terms."""

accum = 0
(a,b) = (1,2)
while b <= 4000000:
    if b % 2 == 0: accum += b
    (a,b) = (b, a+b)
print accum
