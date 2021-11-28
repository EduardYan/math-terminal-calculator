"""
This module have some messages
for show help about the equation to make.
"""

import sys
sys.path.append('..')

from styles.styles import GREEN

HELP_EQUATION_MESSAGE = GREEN + '''
	Type of Ecuation to make:


    Variable to find
    ^                  Equality Sign
    |                  ^
    |                  |
    |                  |
    x operator value 1 = value 2
        |         |            |
        |         |            |
        |         |            |
        ˅         ˅            ˅
        Operator  First Value Second Value
        between
        the value1
        and the
        value 2

	Sample:
	x + value 1 = value 2
        x - 3 = 5

	The operator can be - or +.

'''
