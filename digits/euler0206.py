#!/usr/bin/python
"""Concealed Square

   Find the unique positive integer whose square has the form
   1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit."""

# lower bound = 1010101011 =  ceil(sqrt(1020304050607080900))
# upper bound = 1389026623 = floor(sqrt(1929394959697989900))

# The last digit of the answer must be 0 (and thus the last two digits of the
# square must be 0).

# The penultimate digit of the answer must be either 3 or 7.

# The answer must therefore be of the form 1_______30 or 1_______70.

#from   math import sqrt, ceil
import re

target = re.compile('^1.2.3.4.5.6.7.8.9.0$')

i = 1010101030
while i < 1389026623:
    if target.search(str(i*i)):
        print i
        break
    i += 40
    s = str(i*i)
    if target.search(s):
        print i
        break
    # This attempt at skipping impossible candidates just ends up slowing
    # things down:
    #if s[2] > '2':
        #i = int(ceil(sqrt(1e18 + (int(s[1]) + 1) * 1e17)))
        #i += 30 - i % 100
    #else:
    i += 60
