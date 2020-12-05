#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	num = ''.join(line)
	print('%s\t%s' % (num, None))