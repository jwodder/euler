#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Triangle containment

    Three distinct points are plotted at random on a Cartesian plane, for which
    $-1000\leq x,y\leq 1000$, such that a triangle is formed.

    Consider the following two triangles:

    $$A(-340,495), B(-153,-910), C(835,-947)$$

    $$X(-175,41), Y(-421,-714), Z(574,-645)$$

    It can be verified that triangle ABC contains the origin, whereas triangle
    XYZ does not.

    Using `triangles.txt` (right click and 'Save Link/Target As...'), a 27K
    text file containing the co-ordinates of one thousand "random" triangles,
    find the number of triangles for which the interior contains the origin.

    NOTE: The first two examples in the file represent the triangles in the
    example given above."""

from __future__ import with_statement

qty = 0
with open('data/triangles.txt') as fp:
    for line in fp:
        ax, ay, bx, by, cx, cy = map(int, line.split(','))
        a = (ax,ay)
        b = (bx,by)
        c = (cx,cy)
        sign = 0
        for (v1, v2) in ((a,b), (b,c), (c,a)):
            q = (v1[0] - v2[0]) * v1[1] - (v1[1] - v2[1]) * v1[0]
            # q = (v1-v2)×v1 • ⟨0,0,1⟩
            if q != 0:
                qsign = 1 if q > 0 else -1
                if sign == 0:
                    sign = qsign
                elif sign != qsign:
                    break
        else:
            qty += 1
print qty
