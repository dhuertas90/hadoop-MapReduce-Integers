#!/usr/bin/env python
"""reducer.py"""

import sys

count=0

for line in sys.stdin:
	line = line.strip()
	(numero, null) = line.split('\t', 1)
	count+=1
print ('%s\t%s' % ('Cantidad: ', count))