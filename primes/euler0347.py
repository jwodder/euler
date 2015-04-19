from eulerlib import primeIter, cross

n = 10000000
#n = 100

def powers(p,n):
    pk = p
    while pk <= n:
        yield pk
        pk *= p

accum = 0
for p in primeIter(bound=n//2):
    ppows = list(powers(p,n))
    for q in primeIter(bound=min(p-1,n//p)):
        accum += max(pk * qk for (pk,qk) in cross(ppows, powers(q,n))
                             if pk * qk <= n)
print accum
