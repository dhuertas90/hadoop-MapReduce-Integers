#!/usr/bin/env python
"""mapperE.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	num = ''.join(line)
	print('%s\t%s' % (num, 'E'))