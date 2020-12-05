#!/usr/bin/env python
"""mapperFinal.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	(numero, origen) = line.split('\t',1)
	print ('%s\t%s' % (numero, 1 ))