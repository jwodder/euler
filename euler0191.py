#!/usr/bin/python
"""Prize Strings

   A particular school offers cash rewards to children with good attendance and
   punctuality.  If they are absent for three consecutive days or late on more
   than one occasion then they forfeit their prize.

   During an n-day period a trinary string is formed for each child consisting
   of L's (late), O's (on time), and A's (absent).

   Although there are eighty-one trinary strings for a 4-day period that can be
   formed, exactly forty-three strings would lead to a prize:

       OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
       OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
       AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
       AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
       LAOO LAOA LAAO

   How many "prize" strings exist over a 30-day period?"""

cache = [None] * 31

def nonconsec(n):
    """Returns the number of binary strings of length `n` in which there are no
       occurrences of three consecutive ones"""
    if cache[n] is None:
	if n < 3: cache[n] = 1 << n
	elif n == 3: cache[n] = 7
	else: cache[n] = 2 * nonconsec(n-1) - nonconsec(n-4)
	    # 2 * nonconsec(n-1) - [number of "tripleless" strings of length
	    #                       n-1 that end in two ones = number of
	    #                       tripleless strings of length n-3 that end
	    #                       in a zero = number of tripleless strings of
	    #                       length n-4]
    return cache[n]

print nonconsec(30) + sum(nonconsec(i) * nonconsec(29-i) for i in xrange(30))
