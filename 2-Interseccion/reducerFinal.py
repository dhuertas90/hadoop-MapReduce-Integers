#!/usr/bin/env python
"""reducerFinal.py"""

from operator import itemgetter
import sys

num_act = None

for line in sys.stdin:
	line = line.strip()
	(num, ocurrencia) = line.split('\t', 1)

	if num_act == num:
		print ('%s\t%s' % (num_act, None))
	num_act = num