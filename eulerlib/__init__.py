from   functools import wraps
import heapq
import itertools
import math
import operator
from   bitarray  import bitarray

thesieve = None

def sieve(bound):
    global thesieve
    bound = max(int(bound), 100)
    if not thesieve:
        thesieve = bitarray('00' + '1' * (bound-2))
        thesieve[4::2] = False
        for i in xrange(3, int(bound**0.5)+1, 2):
            if thesieve[i]:
                thesieve[i*i::2*i] = False
    elif bound > len(thesieve):
        oldbound = len(thesieve)
        thesieve.extend('1' * (bound - oldbound))
        thesieve[4::2] = False
        for i in xrange(3, int(bound**0.5)+1, 2):
            if thesieve[i]:
                start = max(i*i, oldbound - oldbound % i)
                thesieve[start::i] = False

def primeIter(amount=None, bound=None):
    if bound is not None:
        sieve(bound)
    primes = (i for i,p in enumerate(thesieve) if p)
    if bound is not None:
        primes = itertools.takewhile(lambda p: p<=bound, primes)
    if amount is not None:
        primes = itertools.islice(primes, amount)
    return primes

def allprimes(startsize=1000, multiplier=10):
    sieve(startsize)
    start = 0
    bound = len(thesieve)
    while True:
        for i in xrange(start, bound):
            if thesieve[i]:
                yield i
        start = bound
        bound *= multiplier
        sieve(bound)

def isPrime(n, presieve=True):
    if n < 2:
        return False
    elif n < len(thesieve):
        return thesieve[n]
    elif presieve:
        sieve(n+1)
        return thesieve[n]
    elif n < len(thesieve)**2:
        return all(n % p for p in itertools.takewhile(lambda q: q*q <= n,
                                                      primeIter()))
    else:
        if any(n % p == 0 for p in primeIter()):
            return False
        x = len(thesieve) - 1
        x = x + 1 - x % 2
        while True:
            if x * x >  n:
                return True
            if n % x == 0:
                return False
            x += 2

def factor(n, presieve=True):
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
            if (p*p > n or isPrime(n, presieve)) and n != 1:
                yield (n,1)
                break
        else:
            yield (n,1)

def divisors(n=None, factors=None, presieve=True):
    if factors is None:
        if n is None:
            raise ValueError('You must supply a non-None argument')
        elif n < 1:
            raise ValueError('`n` argument must be positive')
        factors = factor(n, presieve=presieve)
#   return map(product, itertools.product(*[[p**i for i in range(k+1)]
#                                                 for (p,k) in factors]))
    primals = [[p**i for i in range(k+1)] for (p,k) in factors]
    divs = [1]
    for ps in primals:
        divs = [x*y for x in divs for y in ps]
    return divs

def aliquot(n):
    """Sum of proper divisors of `n`"""
    if n < 1:
        raise ValueError('argument must be positive')
    return product(itertools.starmap(sumPowers, factor(n))) - n

def totient(n):
    if n <= 0:
        raise ValueError('n must be positive')
    return product(p**(k-1) * (p-1) for (p,k) in factor(n))

def product(xs):
    return reduce(operator.mul, xs, 1)

cross = itertools.product

def sumPowers(n,k):
    """Like ``sum(n**i for i in range(k+1))``, but more efficient.  `n` must be
       an integer greater than 1."""
    return (n ** (k+1) - 1) // (n-1)

def modInverse(a,n):
    (u, uc) = (abs(n), 0)
    (l, lc) = (a % u, 1)
    while l > 1:
        (u, uc, l, lc) = (l, lc, u % l, uc - lc * (u//l))
    if l == 1:
        return lc % abs(n)
    else:
        raise ValueError('%d has no multiplicative inverse modulo %d' % (a,n))

def gcd(x,y):
    (a,b) = (abs(x), abs(y))
    if a == 0 or b == 0:
        return a or b
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

def factorial(n):
    return product(xrange(2,n+1))

def nPr(n,r):
    if 0 <= r <= n:
        return product(xrange(n-r+1, n+1))
    else:
        return 0

def nCr(n,r):
    if 0 <= r <= n:
        return nPr(n,r) // factorial(r)
    else:
        return 0

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
    if n < 1:
        raise ValueError
    else:
        return gen(n,n)

_partitionNums = [1, 1, 2, 3, 5, 7]

def partitionNums():
    # Formula taken from <https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas>
    for pn in _partitionNums:
        yield pn
    n = len(_partitionNums)
    while True:
        pn = 0
        k = 1
        while True:
            pentK = (3*k*k - k) // 2
            pentNegK = (3*k*k + k) // 2
            if n >= pentNegK:
                pn += (-1)**((-k-1)%2) * _partitionNums[n-pentNegK]
            if n >= pentK:
                pn += (-1)**((k-1)%2) * _partitionNums[n-pentK]
            else:
                break
            k += 1
        _partitionNums.append(pn)
        yield pn
        n += 1

def isPerfectSquare(n):
    #return perfectSqrt(n) is not None
    x = math.sqrt(n)
    # Testing whether `x` is integral won't work for large values of `n`.
    y = int(x)
    return n in ((y-1)**2, y**2, (y+1)**2)

def intSqrt(n):
    """Returns the floor of the square root of an integral value _exactly_.
       Based on
       <http://www.haskell.org/haskellwiki/Generic_number_type#squareRoot>."""
    if n < 0:
        raise ValueError('negative argument')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        (a,b) = (1,2)
        while n >= b*b:
            (a,b) = (b, b*b)
        x = intSqrt(n // b) * a
        while not (x*x <= n < (x+1)*(x+1)):
            x = (x + n // x) // 2
        return x

def perfectSqrt(n):
    """If the integer `n` is a perfect square, its square root is returned;
       otherwise, `None` is returned."""
    x = intSqrt(n)
    return x if x*x == n else None

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

def subsets(xs, nonempty=False, proper=False):
    """Returns an iterator over all subsets of the iterable `xs` as tuples.  If
       `nonempty` is `True`, only nonempty subsets are returned; if `proper` is
       `True`, only proper subsets are returned."""
    xs = tuple(xs)
    selectors = [False] * len(xs)
    while True:
        if not (nonempty and not any(selectors)) and \
           not (proper and all(selectors)):
            yield tuple(itertools.compress(xs, selectors))
        for i in xrange(len(selectors)):
            selectors[i] = not selectors[i]
            if selectors[i]:
                break
        else:
            break

def sprintFFraction(d, num, denom):
    """Converts ``num / denom`` to a string of the form ``[-]d.dddd``
       containing exactly `n` digits after the decimal place, rounded to the
       nearest ``10**-n``"""
    if d < 0:
        raise ValueError('d must be nonnegative')
    sign = ''
    if num == 0:
        return '0' + ('.' + '0'*d if d > 0 else '')
    elif num < 0 and denom < 0:
        num *= -1
        denom *= -1
    elif num < 0 or denom < 0:
        num = abs(num)
        denom = abs(denom)
        sign = '-'
    if d == 0:
        return sign + str(num // denom + (num * 2 >= denom))
    else:
        charac, mantis = divmod(num, denom)
        mantis = (mantis * 10**(d+1)) // denom
        return sign + '%d.%0*d' % (charac, d, mantis // 10 + (mantis % 10 >= 5))

def mulsInRange(n, a, b):
    """Returns the number of multiples of `n` in ``range(a,b)``.  All arguments
       must be nonnegative integers with ``n>0`` and ``b>=a``."""
    return (b - a + (a-1) % n) // n
    #return (b-1)//n - (a-1)//n

def nextMul(a,b):
    """Returns the next multiple of `a` greater than `b`.  Both arguments must
       be positive integers."""
    return a + b - b % a

def nextEqMul(a,b):
    """Returns the smallest multiple of `a` greater than or equal to `b`.  Both
       arguments must be positive integers."""
    return a + b - (b % a or a)

def memoize(f):
    f.cache = {}
    @wraps(f)
    def wrapper(*args):
        if args not in f.cache:
            f.cache[args] = f(*args)
        return f.cache[args]
    return wrapper

def nth(iterable, n, default=None):
    # From <https://docs.python.org/2.7/library/itertools.html#recipes>
    return next(itertools.islice(iterable, n, None), default)

def generateAsc(init, mknext):
    queue = list(init)
    queue.sort()
    while queue:
        node = heapq.heappop(queue)
        yield node
        for n in mknext(node):
            heapq.heappush(queue, n)
