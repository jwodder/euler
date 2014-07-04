#!/usr/bin/python
import primes

factors = [0] * 20
accum = 1
for i in range(1, 21):
    for p,k in primes.factor(i, [2,3,5,7,11,13,17,19]):
	if k > factors[p-1]:
	    accum *= p ** (k - factors[p-1])
	    factors[p-1] = k
print accum
