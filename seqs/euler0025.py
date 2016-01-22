#!/usr/bin/python
r"""1000-digit Fibonacci number

    The Fibonacci sequence is defined by the recurrence relation:

    $$F_n = F_{n-1} + F_{n-2}\mbox{, where } F_1 = 1 \mbox{ and } F_2 = 1.$$

    Hence the first 12 terms will be:

    \begin{eqnarray*}
    F_1 & = & 1 \\
    F_2 & = & 1 \\
    F_3 & = & 2 \\
    F_4 & = & 3 \\
    F_5 & = & 5 \\
    F_6 & = & 8 \\
    F_7 & = & 13 \\
    F_8 & = & 21 \\
    F_9 & = & 34 \\
    F_{10} & = & 55 \\
    F_{11} & = & 89 \\
    F_{12} & = & 144
    \end{eqnarray*}

    The 12th term, $F_{12}$, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?"""

from math import ceil, log10, sqrt

__tags__ = ['Fibonacci numbers', 'number of digits']

def solve():
    # ceil(log(10**999 * sqrt(5), phi))
    return int(ceil((999 + log10(sqrt(5))) / log10((1+sqrt(5))/2)))

if __name__ == '__main__':
    print solve()
