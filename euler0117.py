#!/usr/bin/python
cache = [None] * 51

def repl(i):
    if cache[i] is None:
        cache[i] = 1 + sum(repl(j) for sz in [2,3,4] for j in xrange(i-sz+1))
    return cache[i]

print repl(50)
