#!/usr/bin/env python
"""mapperA.py"""

import sys
"""
lista_param = sys.argv[1]
lista_elem = []


for linea in lista_param:

	linea = linea.strip()
	numero = ''.join(linea)

	if numero in lista_elem:
		print ('%s\t%s' % (numero, 'SI'))
	else:
		print ('%s\t%s' % (numero, 'NO'))
"""
for line in sys.stdin:
	line = line.strip()
	num = ''.join(line)
	print('%s\t%s' % (num, 'A'))