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

lengths = [0] * 1000
lengths[0] = len('one')
lengths[1] = len('two')
lengths[2] = len('three')
lengths[3] = len('four')
lengths[4] = len('five')
lengths[5] = len('six')
lengths[6] = len('seven')
lengths[7] = len('eight')
lengths[8] = len('nine')
lengths[9] = len('ten')
lengths[10] = len('eleven')
lengths[11] = len('twelve')
lengths[12] = len('thirteen')
lengths[13] = len('fourteen')
lengths[14] = len('fifteen')
lengths[15] = len('sixteen')
lengths[16] = len('seventeen')
lengths[17] = len('eighteen')
lengths[18] = len('nineteen')
lengths[19] = len('twenty')
lengths[29] = len('thirty')
lengths[39] = len('forty')
lengths[49] = len('fifty')
lengths[59] = len('sixty')
lengths[69] = len('seventy')
lengths[79] = len('eighty')
lengths[89] = len('ninety')

def numberLength(n):
    if lengths[n-1] == 0:
	lastTwo = n % 100
	if lastTwo != 0:
	    if lengths[lastTwo-1] == 0:
		lengths[lastTwo-1] = lengths[lastTwo - lastTwo%10 - 1] \
				   + lengths[lastTwo%10 - 1]
	    lengths[n-1] = lengths[lastTwo-1]
	firstTwo = n // 100
	if firstTwo != 0:
	    if lastTwo != 0: lengths[n-1] += len('and')
	    hundreds = firstTwo % 10
	    if hundreds != 0:
		lengths[n-1] += lengths[hundreds-1] + len('hundred')
	    thousands = firstTwo // 10
	    if thousands != 0:
		lengths[n-1] += lengths[thousands-1] + len('thousand')
    return lengths[n-1]

print sum(numberLength(i) for i in xrange(1, 1001))
