# SOUscripts
Some scripts for analysing and fetching Statens Offentliga Utredningar (SOU). 

CONTENTS

**soucounter.py** 
- A little script for generating Years and Numbers of SOU reports. 

**googlesou.py**
- A script that uses the generating function of soucounter.py and then sends these results to Google and returns search hit URLs. This script needs "google" by Mario Vilas: https://github.com/MarioVilas/google

**soukarta.py**

– A script that takes names of places (towns, countries, counties etc.) and requests longitute and latitude from Google's location API. Finally it plots these locations on a world map. 
Usage: The script takes one argument (a file). Run with the included testfile as: 

```
python soukarta.py SOU100utf.txt
```