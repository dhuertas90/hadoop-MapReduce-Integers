#!/usr/bin/env python
"""mapperDiferencia.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.split()
	if len(line) == 1:
		#conjunto A, B o C
		print ('%s\t%s' % (line[0], sys.argv[1]))
	else:
		#conjunto UNION
		print ('%s\t%s' % (line[0], sys.argv[2]))