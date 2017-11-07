#!/usr/bin/python

import sys

count = 0
for data in sys.stdin:
    if "/assets/js/the-associates.js" == data.strip():
	count += 1
print(count)
