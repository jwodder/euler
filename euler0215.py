#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Crack-free Walls

    Consider the problem of building a wall out of $2\times 1$ and $3\times 1$
    bricks (horizontal×vertical dimensions) such that, for extra strength, the
    gaps between horizontally-adjacent bricks never line up in consecutive
    layers, i.e. never form a "running crack".

    For example, the following $9\times 3$ wall is not acceptable due to the
    running crack shown in red:

    ![](https://projecteuler.net/project/images/p215_crackfree.gif)

    There are eight ways of forming a crack-free $9\times 3$ wall, written
    $W(9,3) = 8$.

    Calculate $W(32,10)$."""

__tags__ = ['graph traversal', 'partitions', 'partition of an interval']

def crackless(n, start, cracks):
    if n == start:
        yield ()
    else:
        for w in [2,3]:
            start2 = start+w
            if start2 == n:
                yield ()
            elif start2 < n:
                if not cracks:
                    cracks2 = cracks
                elif start2 > cracks[0]:
                    cracks2 = cracks[1:]
                    if cracks2 and start2 == cracks2[0]:
                        continue
                elif start2 == cracks[0]:
                    continue
                else:
                    cracks2 = cracks
                for cs in crackless(n, start2, cracks2):
                    yield (start2,) + cs

width = 32
height = 10

def solve():
    paths = {row: 1 for row in crackless(width, 0, ())}
    beneath = {row: list(crackless(width, 0, row)) for row in paths}
    for _ in xrange(height-1):
        paths = {row: sum(paths[b] for b in beneath[row]) for row in paths}
    return sum(paths.itervalues())

if __name__ == '__main__':
    print solve()
