#!/usr/bin/python
"""Sub-string divisibility

   The number, 1406357289, is a 0 to 9 pandigital number because it is made up
   of each of the digits 0 to 9 in some order, but it also has a rather
   interesting sub-string divisibility property.

   Let $d_1$ be the 1st digit, $d_2$ be the 2nd digit, and so on.  In this way,
   we note the following:

   - $d_2d_3d_4=406$ is divisible by 2
   - $d_3d_4d_5=063$ is divisible by 3
   - $d_4d_5d_6=635$ is divisible by 5
   - $d_5d_6d_7=357$ is divisible by 7
   - $d_6d_7d_8=572$ is divisible by 11
   - $d_7d_8d_9=728$ is divisible by 13
   - $d_8d_9d_{10}=289$ is divisible by 17

   Find the sum of all 0 to 9 pandigital numbers with this property."""

from itertools import permutations  # requires Python v.2.6+

def insert(tup, i, d): return tup[:i] + (d,) + tup[i:]

def potentials():
    for digits in permutations('12346789'):
        yield ''.join(insert(insert(digits, 3, '0'), 5, '5'))
        if digits[3] in '2468':
            for i in xrange(4,9):
                digits2 = insert(digits, i, '0')
                yield ''.join(insert(digits2, 5, '5'))
                digits2 = insert(digits, i, '5')
                yield ''.join(insert(digits2, 5, '0'))
        if digits[2] in '2468':
            for i in xrange(0,3):
                if i != 0:
                    digits2 = insert(digits, i, '0')
                    yield ''.join(insert(digits2, 5, '5'))
                digits2 = insert(digits, i, '5')
                yield ''.join(insert(digits2, 5, '0'))

accum = 0
for pandigital in potentials():
    #if pandigital[0] == '0': continue
    #if pandigital[3] not in '02468' or pandigital[5] not in '05': continue
    if int(pandigital[2:5]) % 3 == 0 \
        and int(pandigital[4:7]) % 7 == 0 \
        and int(pandigital[5:8]) % 11 == 0 \
        and int(pandigital[6:9]) % 13 == 0 \
        and int(pandigital[7:10]) % 17 == 0:
        accum += int(pandigital)
print accum
