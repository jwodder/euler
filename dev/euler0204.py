import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import nPrimes, cross, product

limit = 1000000000
primes = list(nPrimes(amount=None, bound=100))

primePowers = []
for p in primes:
    powers = [1]
    x = p
    while x <= limit:
	powers.append(x)
	x *= p
    primePowers.append(powers)

qty = 0

#for factors in cross(*primePowers):
#    if product(factors) <= limit:
#	qty += 1

indices = [0] * len(primePowers)
while True:
    x = product(powers[i] for (powers, i) in zip(primePowers, indices))
    if x <= limit:
	qty += 1
    else:
	for i in range(len(indices)-1, -1, -1):
	    if indices[i] == 0:
	        indices[i] = len(primePowers[i])
	    else:
	        indices[i] = len(primePowers[i])
		break
    for i in range(len(indices)-1, -1, -1):
	indices[i] += 1
	if indices[i] >= len(primePowers[i]):
	    indices[i] = 0
	else:
	    break
    else:
	break

print qty
