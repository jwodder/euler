from   __future__ import division
import operator

class Polynomial(object):
    def __init__(self, *p):
        if len(p) == 1 and isinstance(p[0], Polynomial):
            self._coef = p[0]._coef
        elif len(p) == 1 and isinstance(p[0], (list, tuple)):
            self._coef = tuple(p[0])
        else:
            self._coef = p
        i = len(self._coef) - 1
        while i >= 0 and self._coef[i] == 0:
            i -= 1
        self._coef = self._coef[0:i+1]

    def __add__(self, other):
        p = self._coef
        q = Polynomial(other)._coef
        if len(p) < len(q):
            p += (0,) * (len(q) - len(p))
        elif len(q) < len(p):
            q += (0,) * (len(p) - len(q))
        return Polynomial(map(operator.add, p, q))

    __radd__ = __add__

    def __mul__(self, other):
        return sum((Polynomial(other).scale(x) << i
                    for i,x in enumerate(self._coef) if x != 0), Polynomial())

    __rmul__ = __mul__

    def scale(self, c):
        return Polynomial(map(lambda x: x*c, self._coef))

    def __call__(self, x):
        return reduce(lambda ac, c: ac*x + c, self._coef[::-1], 0)

    @classmethod
    def lagrange(cls, points):
        terms = []
        for (xi, yi) in points:
            newTerm = (yi,)
            for (j, (xj, _)) in enumerate(terms):
                terms[j] *= cls((-xi/(xj-xi), 1/(xj-xi)))
                newTerm  *= cls((-xj/(xi-xj), 1/(xi-xj)))
            terms.append((xi, newTerm))
        return sum((t for _,t in terms), Polynomial())

    def __lshift__(self, n):  # Multiply by x^n (n>=0)
        if n < 0:
            raise ValueError('negative argument')
        elif n == 0 or not self:
            return self
        else:
            return Polynomial((0,) * n + self._coef)

    def __hash__(self): return hash(self._coef)

    def __nonzero__(self): return bool(self._coef)

    def __repr__(self): return 'Polynomial(%r)' % (self._coef,)

    def __str__(self):
        if not self:
            return '0'
        else:
            s = ''
            for i in xrange(len(self._coef)-1, -1, -1):
                c = self._coef[i]
                if c == 0: continue
                if c == -1 and i != 0:
                    s += ' - ' if s else '-'
                elif c != 1 or i == 0:
                    if s:
                        try:
                            s += ' - ' + str(-c) if c<0 else ' + ' + str(c)
                        except TypeError:
                        # "no ordering relation is defined for complex numbers"
                            s += ' + (' + str(c) + ')'
                    else:
                        s = str(c)
                if i != 0:
                    s += 'x'
                    if i != 1:
                        s += '^' + str(i)
            return s

    def __pos__(self): return self

    def __neg__(self): return self.scale(-1)

    def derivative(self):
        return Polynomial(tuple(c*(i+1) for i,c in enumerate(self._coef[1:])))

    def integral(self):  # No constant of integration is added.
        return Polynomial((0,)+tuple(c/(i+1) for i,c in enumerate(self._coef)))

    ### Does this handle the zero polynomial correctly?
    def degree(self): return len(self._coef) - 1

    def __sub__(self, other): return self + (-other)

    def __rsub__(self, other): return other + (-self)

    def __cmp__(self, other):
        c1 = cmp(type(self), type(other))
        if c1 != 0:
            return c1
        p = self._coef[::-1]
        q = other._coef[::-1]
        if len(p) < len(q):
            p = (0,) * (len(q) - len(p)) + p
        elif len(q) < len(p):
            q = (0,) * (len(p) - len(q)) + q
        return cmp(p,q)

    def coef(self, n): return self._coef[n] if 0 <= n < len(self._coef) else 0

    def coefs(self): return self._coef


Polynomial.X = Polynomial((0,1))  ### Should this be a module global instead?

def bezier(end1, cntrl1, cntrl2, end2):
    # takes four points (pairs of numbers) and returns a pair of Polynomials
    (x1, y1) = end1    # endpoint 1
    (x2, y2) = cntrl1  # control point 1
    (x3, y3) = cntrl2  # control point 2
    (x4, y4) = end2    # endpoint 2
    bx = 3 * (x2 - x1)
    cx = 3 * (x3 - x2) - bx
    dx = x4 - x1 - bx - cx
    by = 3 * (y2 - y1)
    cy = 3 * (y3 - y2) - by
    dy = y4 - y1 - by - cy
    return (Polynomial((x1, bx, cx, dx)), Polynomial((x2, by, cy, dy)))

def unbezier(p,q):
    # takes two polynomials and returns a tuple of four points
    if p.degree() > 3 or q.degree() > 3:
        raise ValueError('arguments must have degree at most 3')
    (x1, bx, cx, dx) = (p._coef + (0,0,0,0))[:4]
    (y1, by, cy, dy) = (q._coef + (0,0,0,0))[:4]
    x2 = x1 + bx / 3
    y2 = y1 + by / 3
    return ((x1, y1),
            (x2, y2),
            (x2 + (bx + cx) / 3, y2 + (by + cy) / 3),
            (x1 + bx + cx + dx, y1 + by + cy + dy))
