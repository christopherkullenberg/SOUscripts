# -*- coding: utf8 -*-
# SOUcounter.py
# Generate Year and Numbers for Statens Offentliga Utredningar.

import itertools


## Define ranges of SOU reports. 
years = range(1996, 2016)
numbers = range(0,200)
result = ""


## Here the numbers are iterated over the years
for year in years:
    for y, n in itertools.product([year], numbers):
        result += "SOU %d:%d, " % (y, n)    # Comma separated list
        #result += "SOU %d:%d\n" % (y, n)    # Newline list 


## Print the results. Comment/uncomment above for type of list.
print result


