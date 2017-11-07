#!/usr/bin/python

import sys

dictionaryOfPath = {}

for line in sys.stdin:
	data = line.strip()
   if not data in dictionaryOfPath:
        	dictionaryOfPath[data] = 1
    	else:
        	dictionaryOfPath[data] = dictionaryOfPath[data]+ 1
        
count, pathHitted = max(zip(dictionaryOfPath.values(), dictionaryOfPath.keys()))
print count
