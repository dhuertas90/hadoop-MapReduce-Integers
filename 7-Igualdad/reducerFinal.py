#!/usr/bin/env python
"""reducerFinal.py"""

import sys

num_act = None
ocurrencias = 0
result = 'SI'

for line in sys.stdin:
	line = line.strip()
	(num, origen) = line.split('\t', 1)

	if num_act == num:
		ocurrencias+=1
	else:
		if ocurrencias == 1:
			result = 'NO'
			break
		num_act = num
		ocurrencias = 1

if ocurrencias == 1:
	result = 'NO'
print('%s\t%s' % ('Son iguales:', result))