#!/usr/bin/python
"""Number letter counts

   If the numbers 1 to 5 are written out in words: one, two, three, four, five,
   then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.

   If all the numbers from 1 to 1000 (one thousand) inclusive were written out
   in words, how many letters would be used?

   **NOTE:** Do not count spaces or hyphens.  For example, 342 (three hundred
   and forty-two) contains 23 letters and 115 (one hundred and fifteen)
   contains 20 letters.  The use of "and" when writing out numbers is in
   compliance with British usage."""

__tags__ = ['text', 'English']

lengths    = [None] * 1001
lengths[0] = 0  # empty string
lengths[1] = len('one')
lengths[2] = len('two')
lengths[3] = len('three')
lengths[4] = len('four')
lengths[5] = len('five')
lengths[6] = len('six')
lengths[7] = len('seven')
lengths[8] = len('eight')
lengths[9] = len('nine')
lengths[10] = len('ten')
lengths[11] = len('eleven')
lengths[12] = len('twelve')
lengths[13] = len('thirteen')
lengths[14] = len('fourteen')
lengths[15] = len('fifteen')
lengths[16] = len('sixteen')
lengths[17] = len('seventeen')
lengths[18] = len('eighteen')
lengths[19] = len('nineteen')
lengths[20] = len('twenty')
lengths[30] = len('thirty')
lengths[40] = len('forty')
lengths[50] = len('fifty')
lengths[60] = len('sixty')
lengths[70] = len('seventy')
lengths[80] = len('eighty')
lengths[90] = len('ninety')

def numberLength(n):
    if lengths[n] is None:
        ab, cd = divmod(n, 100)
        if lengths[cd] is None:
            d = n % 10
            lengths[cd] = lengths[cd-d] + lengths[d]
        lengths[n] = lengths[cd]
        a,b = divmod(ab, 10)
        if ab != 0 and cd != 0:
            lengths[n] += len('and')
        if b != 0:
            lengths[n] += lengths[b] + len('hundred')
        if a != 0:
            lengths[n] += lengths[a] + len('thousand')
    return lengths[n]

def solve():
    return sum(map(numberLength, xrange(1, 1001)))

if __name__ == '__main__':
    print solve()
