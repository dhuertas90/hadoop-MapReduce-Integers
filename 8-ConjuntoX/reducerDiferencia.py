#!/usr/bin/env python
"""reducerDiferencia.py"""

import sys

origen_act = 'None'
num_act = None
ocurrencias = 0

for line in sys.stdin:
	line = line.strip()
	(num, origen) = line.split('\t', 1)

	if num_act == num:
		ocurrencias+=1
	else:
		if ocurrencias==1 and origen_act != 'UNION':
			print('%s\t%s' % (num_act, 'X'))
		num_act = num
		ocurrencias = 1
		origen_act = origen

if ocurrencias==1 and origen_act != 'UNION':
	print('%s\t%s' % (num_act, 'X'))