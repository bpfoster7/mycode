#!/usr/bin/env python3

import requests
from lxml import  html
r = requests.get('https://frederick.craigslist.org/d/free-stuff/search/zip')

#print (r.text)

test = html.fromstring(r.text)
print (test)
