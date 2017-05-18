#!usr/bin/env python



import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url) .read()
soup = BeatifulSoup(html)

tags = soup('a')

for tag in tags:
	print tag.get('href' , None)
