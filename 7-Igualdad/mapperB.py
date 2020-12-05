#!/usr/bin/env python
"""mapperB.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	numero = ''.join(line)	
	print ('%s\t%s' % (numero, 'B'))