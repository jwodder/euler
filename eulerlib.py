import itertools
import operator

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
	    yield (n, 1)

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
