#!/usr/bin/python
"""Double-base palindromes

   The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both
   bases.

   Find the sum of all numbers, less than one million, which are palindromic in
   base 10 and base 2.

   (Please note that the palindromic number, in either base, may not include
   leading zeros.)"""

__tags__ = ['digits', 'binary', 'palindromic number']

def solve():
    accum = 0
    for num in range(1,10):  # special case for single-digit numbers
        binnum = bin(num).lstrip('0b')
        if binnum == binnum[::-1]:
            accum += num
    for digits in range(2,7):
        leadlen = digits // 2
        middle = '0123456789' if digits % 2 else ['']
        for p1 in xrange(10**(leadlen-1), 10**leadlen):
            part1 = str(p1)
            for part2 in middle:
                num = int(part1 + part2 + part1[::-1])
                binnum = bin(num).lstrip('0b')
                if binnum == binnum[::-1]:
                    accum += num
    return accum

if __name__ == '__main__':
    print solve()
