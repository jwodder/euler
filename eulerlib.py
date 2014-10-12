from   bisect import bisect_left
import itertools
import math
import operator

primeCache = [2,3]

def primeIter(amount=None, bound=None):
    """Returns an iterator over the first `amount` prime numbers less than or
       equal to `bound`, or over all primes if both parameters are `None`"""
    def _isPrime(n):
	for k in primeCache[1:]:
	    if k * k >  n: return True
	    if n % k == 0: return False
    i=0
    while amount is None or i < amount:
	if i < len(primeCache):
	    yield primeCache[i]
	else:
	    j = primeCache[-1] + 2
	    while not _isPrime(j): j += 2
	    primeCache.append(j)
	    if bound is None or j <= bound:
		yield j
	    else:
		return
	i += 1

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
	    if p*p > n and n != 1:
		yield (n, 1)
		break
	else:
	    yield (n, 1)

def isPrime(n):
    if n < 2:
	return False
    elif n <= primeCache[-1]:
	return primeCache[bisect_left(primeCache, n)] == n
    else:
	for p in primeIter():
	    if p * p >  n: return True
	    if n % p == 0: return n == p

def product(xs): return reduce(operator.mul, xs, 1)

def divisors(n):
    if n < 1: raise ValueError('argument must be positive')
    primals = [[p**i for i in range(k+1)] for (p,k) in factor(n)]
    divs = [1]
    for ps in primals:
	divs = [x*y for x in divs for y in ps]
    return divs

def sumPowers(n,k):
    """Like ``sum(n**i for i in range(k+1))``, but more efficient.

       `n` must be an integer greater than 1."""
    return (n ** (k+1) - 1) // (n-1)

def aliquot(n):
    """Sum of proper divisors of `n`"""
    if n < 1: raise ValueError('argument must be positive')
    #return product(sumPowers(*pk) for pk in factor(n)) - n
    return product(itertools.starmap(sumPowers, factor(n))) - n

# cross = itertools.product  # Python v.2.6+
def cross(*args):
    args = map(tuple, args)
    if not all(args): return
    indices = [0] * len(args)
    while True:
	yield tuple(arg[i] for (arg, i) in zip(args, indices))
	for i in range(len(indices)-1, -1, -1):
	    indices[i] += 1
	    if indices[i] >= len(args[i]):
		indices[i] = 0
	    else:
		break
	else:
	    break

def modInverse(a,n):
    (u, uc) = (abs(n), 0)
    (l, lc) = (a % u, 1)
    while l > 1:
	(u, uc, l, lc) = (l, lc, u % l, uc - lc * (u//l))
    if l == 1:
	return lc % abs(n)
    else:
	raise ValueError('%d has no multiplicative inverse modulo %d' % (a,n))

def totient(n):
    if n <= 0: raise ValueError('n must be positive')
    return product(p**(k-1) * (p-1) for (p,k) in factor(n))

def gcd(x,y):
    (a,b) = (abs(x), abs(y))
    if   a == 0 and b == 0: return 0
    elif a == 0 or  b == 0: return a or b
    while b != 0:
	(a,b) = (b, a % b)
    return a

def lcm(x,y):
    d = gcd(x,y)
    return 0 if d == 0 else abs(x*y) // d

def reduceFrac(x,y):
    if x <= 0 and y <= 0:
	(x,y) = (-x, -y)
    d = gcd(x,y)
    return (0,0) if d == 0 else (x // d, y // d)

def factorial(n): return product(xrange(2,n+1))

def nPr(n,r): return product(xrange(n-r+1, n+1))

def nCr(n,r): return nPr(n,r) // factorial(r)

def convergents(cfiter):
    """Returns the successive convergents of a given simple continued fraction
       as ``(numerator, denominator)`` pairs"""
    cfiter = iter(cfiter)
    a0 = cfiter.next()
    a1 = cfiter.next()
    (pk, qk) = (a0, 1)
    (pk1, qk1) = (a0 * a1 + 1, a1)
    yield reduceFrac(pk, qk)
    yield reduceFrac(pk1, qk1)
    for a in cfiter:
	((pk,qk), (pk1, qk1)) = ((pk1, qk1), (a * pk1 + pk, a * qk1 + qk))
	yield reduceFrac(pk1, qk1)

def partitions(n):
    def gen(qty, mx):
	if qty == 0:
	    yield ()
	else:
	    for i in range(min(qty,mx), 0, -1):
		for xs in gen(qty-i, i):
		    yield (i,) + xs
    if n < 1: raise ValueError
    else: return gen(n,n)

def isPerfectSquare(n):
    x = math.sqrt(n)
    #return x == int(math.modf(x)[1])
    return x == math.modf(x)[1]
    #return math.modf(x)[0] == 0
    #return x == math.floor(x)
    #return x == math.trunc(x)  # Python v.2.6+
    #return x.is_integer()  # Python v.2.6+

def dijkstraLength(start, end, neighbors, length):
    """Returns the length of the shortest path from `start` to `end`.
       `neighbors` must be a function that takes a vertex and returns an
       iterable of all of its neighbors.  `length` must be a function that
       takes two neighboring vertices `x` and `y` and returns the length of the
       edge from `x` to `y`.  All vertices must be hashable."""
    visited = set()
    distances = {start: 0}
    current = start
    while True:
	for p in neighbors(current):
	    if p not in visited:
		newdist = distances[current] + length(current, p)
		olddist = distances.get(p, None)
		if olddist is None or olddist > newdist:
		    distances[p] = newdist
	visited.add(current)
	if end in visited:
	    return distances[end]
	visitable = [p for p in distances if p not in visited]
	if visitable:
	    current = min(visitable, key=lambda p: distances[p])
	else:
	    raise ValueError('No route to endpoint')
