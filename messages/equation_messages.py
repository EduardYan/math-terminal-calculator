"""
This module have some messages
for show help about the equation to make.
"""

import sys
sys.path.append('..')

from styles.styles import GREEN

HELP_EQUATION_MESSAGE = GREEN + '''
	Type of Ecuation to make:

	x -----> variable to find.
	value 1 ----> first value.
	operator -----> operator for operate between the first value and the second value.
	value2 -----> second value.

	Sample:
	x + value 1 = value 2

	The operator can be - or +.

'''
