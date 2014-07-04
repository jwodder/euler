import itertools

primeCache = [2,3]

def primeIter():
    def isPrime(n):
	for k in primeCache[1:]:
	    if k * k >  n: return True
	    if n % k == 0: return False
    i=0
    while True:
	if i < len(primeCache):
	    yield primeCache[i]
	else:
	    # This is so not thread-safe.
	    j = primeCache[-1] + 2
	    while not isPrime(j): j += 2
	    primeCache.append(j)
	    yield j
	i += 1

def nPrimes(amount=1000, bound=None):
    """Returns an iterator over the first `amount` prime numbers less than or
       equal to `bound`"""
    if amount is None and bound is None:
	return iter([])
    primes = primeIter()
    if bound is not None:
	primes = itertools.takewhile(lambda p: p<=bound, primes)
    if amount is not None:
	primes = itertools.islice(primes, amount)
    return primes

def factor(n, primal=None):
    if n == 0:
	yield (0,1)
    else:
	if primal is None:
	    primal = primeIter()
	if n < 0:
	    yield (-1, 1)
	    n *= -1
	for p in primal:
	    if n == 1: break
	    k=0
	    while n % p == 0:
		n //= p
		k += 1
	    if k > 0: yield (p,k)
	else:
	    yield (n, 1)  ### ???
