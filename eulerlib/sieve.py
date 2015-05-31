import itertools

thesieve = []

class NBeyondSieveError(Exception):
    def __init__(self, n):
        self.n = n
        self.sievesize = len(thesieve)
        super(NBeyondSieveError, self).__init__(n)

    def __str__(self):
        return 'Value %d exceeds size of precomputed sieve (%d)' \
                % (self.n, self.sievesize)

def sieve(bound):
    global thesieve
    if bound < 2:
        thesieve = [False] * bound
    else:
        thesieve = [False, False] + [True] * (bound - 2)
        for i in xrange(bound):
            if thesieve[i]:
                for j in xrange(2*i, bound, i):
                    thesieve[j] = False

def primeIter(amount=None, bound=None):
    primes = (i for i,p in enumerate(thesieve) if p)
    if bound is not None:
        #if bound > len(thesieve): raise NBeyondSieveError(bound) ???
        primes = itertools.takewhile(lambda p: p<=bound, primes)
    if amount is not None:
        primes = itertools.islice(primes, amount)
    return primes

def isPrime(n):
    if n < 0:
        return False
    elif n < len(thesieve):
        return thesieve[n]
    else:
        raise NBeyondSieveError(n)

def isKnownPrime(n):
    return 0 <= n < len(thesieve) and thesieve[n]

def factor(n):
    if n == 0:
        yield (0,1)
    else:
        if n < 0:
            yield (-1, 1)
            n *= -1
        for p in primeIter():
            if n == 1:
                break
            k=0
            while n % p == 0:
                n //= p
                k += 1
            if k > 0:
                yield (p,k)
            if (p*p > n or isKnownPrime(n)) and n != 1:
                yield (n,1)
                break
        else:
            yield (n,1)
