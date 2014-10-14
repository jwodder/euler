import sys
sys.path.insert(1, sys.path[0] + '/..')
from eulerlib import factor, modInverse, cross

def I(n):
    terms = []
    for (p,k) in factor(n):
	if p % 2 == 0 and k>1:
	    residues = (1, -1, (1<<k-1)-1, (1<<k-1)+1)
	else:
	    residues = (1, -1)
	pk = p**k
	coef = n // pk * modInverse(n // pk, pk)
	terms.append(map(lambda x: x*coef, residues))
    return max(filter(lambda x: x != n-1, (sum(res) % n for res in cross(*terms))))

#print sum(I(i) for i in xrange(3, 20000001))
for i in xrange(3, 20000001):
    print '%d\t%d' % (i, I(i))
