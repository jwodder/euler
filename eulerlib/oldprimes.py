from bisect      import bisect_left
from collections import deque

primeCache = [2,3]

def primeIter(amount=None, bound=None):
    """Returns an iterator over the first `amount` prime numbers less than or
       equal to `bound`, or over all primes if both parameters are `None`"""
    def _isPrime(n):
        for k in primeCache:
        # I originally wrote `for k in primeCache[1:]:` here in order to skip
        # the unnecessary check for oddness, thinking that Python would be
        # smart about iterating over a slice.  It is not, and writing just `for
        # k in primeCache:` gives a massive speedup.
            if k * k >  n: return True
            if n % k == 0: return False
    i=0
    while amount is None or i < amount:
        if i < len(primeCache):
            p = primeCache[i]
        else:
            p = primeCache[-1] + 2
            while not _isPrime(p): p += 2
            primeCache.append(p)
        if bound is None or p <= bound:
            yield p
        else:
            return
        i += 1

def precalPrimes(amount=None, bound=None):
    """Precalculates the first `amount` prime numbers less than or equal to
       `bound`"""
    if amount is None and bound is None:
        raise ValueError('At least one argument must be non-None')
    # based on the `consume` recipe in the itertools documentation
    deque(primeIter(amount=amount, bound=bound), maxlen=0)

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
            if (p*p > n or (n <= primeCache[-1] and isPrime(n))) and n != 1:
                yield (n,1)
                break
        else:
            yield (n,1)

def isPrime(n):
    """Returns `True` iff the given integer is prime.  After returning, all
       primes less than or equal to the square root of the argument will have
       been added to the prime cache if they were not already present."""
    if n < 2:
        return False
    elif n <= primeCache[-1]:
        return primeCache[bisect_left(primeCache, n)] == n
    else:
        for p in primeIter():
            if p * p >  n: return True
            if n % p == 0: return n == p

def isPrime2(n):
    """Like `isPrime`, except that no new primes are added to the prime cache.
       This may be faster in some situations."""
    if n < 2:
        return False
    elif n <= primeCache[-1]:
        return primeCache[bisect_left(primeCache, n)] == n
    else:
        for p in primeCache:
            if p * p >  n: return True
            if n % p == 0: return False
        p = primeCache[-1] + 2
        while True:
            if p * p >  n: return True
            if n % p == 0: return n == p
            p += 2
