#!/usr/bin/python
r"""Champernowne's constant

    An irrational decimal fraction is created by concatenating the positive
    integers:

    $$0.12345678910[1]112131415161718192021\ldots$$

    It can be seen that the 12th digit of the fractional part is 1.

    If $d_n$ represents the $n$th digit of the fractional part, find the value
    of the following expression.

    $$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times
    d_{100000} \times d_{1000000}$$"""

__tags__ = ['digits']

def shorter(d):
    """Returns the number of nonnegative integers with fewer than `d` digits"""
    return 0 if d <= 1 else 10**(d-1)

def solve():
    landmarks = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    digits = 1
    consumed = 0
    while landmarks:
        nextSectionLen = digits * (shorter(digits+1) - shorter(digits))
        if consumed + nextSectionLen > landmarks[0]:
            offset = landmarks[0] - consumed
            div, mod = divmod(offset, digits)
            product *= int(str(shorter(digits) + div)[mod])
            landmarks.pop(0)
        else:
            consumed += nextSectionLen
            digits += 1
    return product

if __name__ == '__main__':
    print solve()
