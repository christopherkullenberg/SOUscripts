# -*- coding: utf8 -*-

# GoogleSOU - Generates a list of SOU reports and Googles them. 
# This script requires "google" by Mario Vilas:
# https://github.com/MarioVilas/google
# Note: Using Google too much will probably lead to Google 
# blocking your IP number for a while. 

# Itertools and Google are needed.
import itertools
from google import search

# Define ranges of SOU reports (change accordingly). 
years = range(1997, 2016)
numbers = range(1, 2001)
result = ""

# Here the numbers are iterated over the years
for year in years:
    for y, n in itertools.product([year], numbers):
        result += "%d:%d "  % (y, n)    # Comma separated list

# Split each result to create a list (souresult) for further use.
sresult = result.split(' ')

# Send the SOU numbers from the list to the google search and add "SOU" 
# in front of each number(had to do this here because lists don't like spaces) 
for sou in sresult:
    sou = "SOU %s" % sou
    for url in search(sou, stop=10):
         print "Googling report %r with the results:\n %r" % (sou, url)
