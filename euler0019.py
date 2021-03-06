#!/usr/bin/python
"""Counting Sundays

   You are given the following information, but you may prefer to do some
   research for yourself.

   - 1 Jan 1900 was a Monday.

   - Thirty days has September,
     April, June and November.
     All the rest have thirty-one,
     Saving February alone,
     Which has twenty-eight, rain or shine.
     And on leap years, twenty-nine.

   - A leap year occurs on any year evenly divisible by 4, but not on a century
     unless it is divisible by 400.

   How many Sundays fell on the first of the month during the twentieth century
   (1 Jan 1901 to 31 Dec 2000)?"""

__tags__ = ['calendar']

common = [31, 28] + [31, 30, 31, 30, 31] * 2
leap = common[:]
leap[1] = 29

def solve():
    offset = 2  # 1901-01-01 was a Tuesday
    qty = 0
    for mlen in (common * 3 + leap) * 25:
        offset = (offset + mlen) % 7
        if offset == 0:
            qty += 1
    return qty

if __name__ == '__main__':
    print solve()
