# -*- coding: utf8 -*-

# SOUcounter.py
# Generate Year and Numbers for Statens Offentliga Utredningar
# and create a list (sresult)

# Itertools are needed.
import itertools

# Define ranges of SOU reports (change accordingly). 
years = range(1997, 2016)
numbers = range(1, 11)
result = ""

# Here the numbers are iterated over the years
for year in years:
    for y, n in itertools.product([year], numbers):
        result += "%d:%d "  % (y, n)    # Comma separated list

# Split each result to create a list (sresult) for further use.
sresult = result.split(' ')

#print each number with "SOU " in front.
for sou in sresult:
    print "SOU %s" % sou



