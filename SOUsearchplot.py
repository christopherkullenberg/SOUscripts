# -*- coding: utf8 -*-
"""
About:
    This script reads all SOU reports from 1922-2015 into 
    a Python dictionary and searches them with regular expressions.
    It stores the search results in text files and plots (optional)
    a figure showing the frequency of the search term/word over 
    time. 

Requirements:
    1. A computer with ~3Gb of RAM available. 
    (tested successfully on a 4Gb RAM system)
    This program will run slowly if your hard drive is slow. 

    2. This script requires the "progress bar" module. Install with:
        
        pip install progress

Usage:
    1. Make a directory with all text files in one single
    directory root. Subdirectories are NOT supported. 
    2. Change path on TWO lines, as indicated in the script. 
    3. Use regular expressions for the search.

Data:
    The 5013 text files can be downloaded from this url:
        
        http://data.thehappysociety.net/SOU19972015.zip
    
"""

from os import listdir
import re
import sys
import time
import io
from progress.bar import Bar


print "Läser in textfiler. Detta kan ta lite tid...."
bar = Bar('Laddar till arbetsminnet ', max=8059)

dictionary = {} #This is where all content data is stored. 

# Read files to memory, change path TWICE
for filename in listdir(u"SOU19222015/"): #change path here (1/2)
    with open("SOU19222015/" + filename) as currentfile: #change path here (2/2)
        text = currentfile.read()
        dictionary[filename] = text
    bar.next()
bar.finish()

countdictionary = {}  # This dictionary only stores year and frequency. 
global_search_word = []   # This list only stores the search_word

# Begin the search function
def regexsearch():
    countdictionary.clear()   # Always clear before new search. 
    del global_search_word[:]  # Always clear begore new search.
    print "Välkommen till SOU-sök!"
    search_word = raw_input("    Ange reguljärt uttryck som du vill söka efter (skiftlägeskönsligt): ")
    global_search_word.append(search_word) # To make a global variable, nothing else. 
    outfile = io.open(search_word + '.txt', 'wt', encoding='utf-8')
    for d in dictionary:
        result = re.findall(search_word, dictionary[d], re.UNICODE) # add "| re.IGNORECASE" after re.UNICODE to make case insensitve. This slows down performance. 
        resultcount = len(result)
        result = ', '.join(result)
        if len(result) > 0:
            year = re.findall('(\d\d\d\d)_\d', d) #This extracts the year from filename
            year = ''.join(year) #make clean
            year = year.strip()  #make cleaner
            if year.isdigit():   #verify digit
                newyear = int(year)  #convert to integer
                if newyear < 2015:   #removes occassional buggy years e.g '19451987'
                    countdictionary[newyear] = countdictionary.get(newyear, 0) + resultcount
            print "*" * 20 
            print u"%s \n" % d 
            print u"%s" % result.decode('utf-8')
            outfile.write("\n" + "*" * 10 +"\n" + d + "\n") #writes to file
            outfile.write(result.decode('utf-8'))           #writes to file
            print "The year is %d and there are %d occurences." % (newyear, resultcount)
    print "*" * 20
    outfile.close()
    print countdictionary
    print "Filen sparad som %s.txt" % search_word.decode('utf-8')
    makegraph = raw_input("Vill du göra ett frekvensdiagram (j/n)?> ")
    if makegraph == "j":
        histogram()
    else: 
            print "KLAR! Gör en ny sökning eller tryck CTRL-C för att avsluta." 
    regexsearch()


def histogram():
    import pylab as pl
    import numpy as np
    #Set size of figure, (width,height)
    pl.figure(figsize=(20,10))
    pl.title(u'Resultat för termen: %s' % global_search_word[0].decode('utf-8'))
    X = np.arange(len(countdictionary))
    #X = np.arange(1921.1996)
    pl.bar(X, countdictionary.values(), align='center', width=0.7)
    yearlength = range(1921, 2015)
    pl.xticks(sorted(X), countdictionary.keys(), rotation='vertical')
    ymax = max(countdictionary.values()) + 1
    pl.ylim(0, ymax)
    print "Saving as %s.png" % global_search_word[0].decode('utf-8')
    pl.savefig(global_search_word[0].decode('utf-8') + '.png')
    pl.show()

regexsearch()
