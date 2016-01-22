#!/usr/bin/python
r"""Sum square difference

    The sum of the squares of the first ten natural numbers is,

    $$1^2 + 2^2 + \cdots + 10^2 = 385$$

    The square of the sum of the first ten natural numbers is,

    $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is $3025 - 385 = 2640$.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum."""

__tags__ = ['integer sequences', 'triangle numbers', 'perfect square']

n = 100

def solve():
    return (n*(n+1)//2)**2 - (n * (n+1) * (2*n + 1) // 6)

if __name__ == '__main__':
    print solve()
