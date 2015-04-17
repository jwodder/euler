#!/usr/bin/python
def replacements(n, size):
    cache = [None] * (n+1)
    def repl(i):
        if cache[i] is None:
            cache[i] = 1 + sum(repl(j) for j in xrange(i-size+1))
        return cache[i]
    return repl(n) - 1

print replacements(50,2) + replacements(50,3) + replacements(50,4)
