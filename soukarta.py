# -*- coding: utf-8 -*-
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import GoogleV3
import time 
import re
from sys import argv
import codecs

"""
USAGE: python soukarta.py FILENAME
"""

script, filename = argv

locationlistfile = codecs.open(filename, encoding='utf-8')
f = locationlistfile.readlines()

platser =[]

for line in f:
    platser.append(line)

"""
#Print for debugging. Will however not show correct formatting.
for p in platser:
     print platser 
"""

geolocator = GoogleV3()
 
longlatlist = []

for cities in platser:
    print cities
    location = geolocator.geocode(cities)
    if location != None:
        loco = ((location.latitude, location.longitude))
        longlatlist.append(loco)

        print longlatlist
        time.sleep(5)

print longlatlist



my_map = Basemap(projection='robin', lat_0=50, lon_0=0,
              resolution='l', area_thresh=1000.0)
 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')

lons = []
lats =[]

for coordinate in longlatlist:
    print coordinate[1]
    print coordinate[0]
    lons.append(coordinate[1])
    lats.append(coordinate[0])

x,y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=12)

 
plt.show()

