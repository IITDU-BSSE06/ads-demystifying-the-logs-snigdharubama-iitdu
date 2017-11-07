#!/usr/bin/python

import sys

countTotalHit=0

for line in sys.stdin:
	if "10.99.99.186" == line.strip():
	    countTotalHit = countTotalHit+1
print countTotalHit
