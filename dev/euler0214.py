import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import nPrimes, totient

def length25(p):
    x = p-1
    i = 2
    while x != 1:
	x = totient(x)
	i += 1
    return i == 25

print sum(itertools.ifilter(length25, nPrimes(amount=None, bound=40000000)))
