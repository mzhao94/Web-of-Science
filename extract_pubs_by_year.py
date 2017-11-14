#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:31:48 2017

@author: michellezhao
"""

import requests
import csv
import time
import sys

startTime = time.time()
year = sys.argv[1]
response = requests.get(
    "".join([
        "https://icite.od.nih.gov/api/pubs?year=",
        year,
    ]),
)

links = response.json()["links"]
pub = response.json()["data"]
test = open('test.csv', 'w')

while links.get("next"):
    nextlink = links["next"]
    print(nextlink)
    response = requests.get(nextlink)
    pub = pub + response.json()["data"]
    links = response.json()["links"]

test = open('year_'+year+'.csv', 'w')
csvwriter = csv.writer(test)

count = 0

for t in pub:
	if count == 0:
		header = t.keys()
		csvwriter.writerow(header)
		count += 1
	csvwriter.writerow(t.values())

test.close()




print ('The script took {0} second !'.format(time.time() - startTime))
