#!/usr/bin/python
"""Prime pair sets

   The primes 3, 7, 109, and 673, are quite remarkable.  By taking any two
   primes and concatenating them in any order the result will always be prime.
   For example, taking 7 and 109, both 7109 and 1097 are prime.  The sum of
   these four primes, 792, represents the lowest sum for a set of four primes
   with this property.

   Find the lowest sum for a set of five primes for which any two primes
   concatenate to produce another prime."""

# This assumes that the set with the lowest sum is also the set with the lowest
# maximum element, which turns out to be true.  Hooray for dumb luck!

import sys
sys.path.insert(1, sys.path[0] + '/..')
from   eulerlib.oldprimes import primeIter, isPrime

piter = primeIter()
concatable = dict()

def addPrime():
    p = next(piter)
    pstr = str(p)
    conc = set()
    for q in concatable.iterkeys():
        qstr = str(q)
        if isPrime(int(pstr + qstr)) and isPrime(int(qstr + pstr)):
            conc.add(q)
    concatable[p] = conc
    return (p, conc)

subgraphs = set()

while True:
    p, conc = addPrime()
    new = []
    for kn in subgraphs:
        if all(q in conc for q in kn):
            kn1 = kn + (p,)
            if len(kn1) == 5:
                print sum(kn1)
                sys.exit()
            new.append(kn1)
    subgraphs.update(new)
    for q in conc:
        for r in conc & concatable[q]:
            subgraphs.add((r,q,p))
