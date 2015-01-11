#!/usr/bin/python
r"""Square remainders

    Let $r$ be the remainder when $(a-1)^n + (a+1)^n$ is divided by $a^2$.

    For example, if $a = 7$ and $n = 3$, then $r = 42$: $6^3 + 8^3 = 728\equiv
    42\pmod{49}$.  And as $n$ varies, so too will $r$, but for $a = 7$ it turns
    out that $r_{\max} = 42$.

    For $3\leq a\leq 1000$, find $\sum r_{\max}$."""

# Basic algebra shows that $(a-1)^n + (a+1)^n$ is congruent to $na(-1)^{n-1} +
# (-1)^n + na + 1$ _modulo_ $a^2$.
#  - When $n$ is even, this is equal to 2, which is never the maximum value for
#    $a\geq 3$.
#  - When $n$ is odd, this is equal to $2na$.  Moreover, if $n/a$ has quotient
#    & remainder $p,q$ such that $n = pa + q$, then $2na = 2pa^2 + 2qa$, which
#    is congruent to $2qa$ _modulo_ $a^2$; thus, the only values of $n$ that
#    need to be inspected are those in $[0,a)$.

print sum(max((2*q*a) % (a*a) for q in xrange(1, a, 1 if a%2 else 2))
          for a in xrange(3, 1001))
