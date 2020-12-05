#!/usr/bin/env python
"""reducerFinal.py"""

import sys

num_act = None
origen_act = None
ocurrencias = 0
result = 'SI'

for line in sys.stdin:
	line = line.strip()
	(num, origen) = line.split('\t', 1)

	if num_act == num:
		print('%s\t%s' % (num_act, 'SI'))
		ocurrencias = 0
	else:
		if ocurrencias==1 and origen_act=='E':
			print('%s\t%s' % (num_act, 'NO'))
		num_act = num
		origen_act = origen
		ocurrencias = 1

if ocurrencias==1 and origen_act=='E':
	print('%s\t%s' % (num_act, 'NO'))