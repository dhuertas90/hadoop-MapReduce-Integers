#!/usr/bin/env python
"""reducer.py"""

import sys

num_act = None

for line in sys.stdin:
	line = line.strip()
	(num, origen) = line.split('\t', 1)
	
	if (num_act == num):
		continue
	else:
		if (num_act != None):
			print ('%s\t%s' % (num_act, origen))
		num_act = num

if (num_act == num):
	print ('%s\t%s' % (num_act, origen))