"""
This module have messages for show
help to user
"""

import sys
sys.path.append('..')

from styles.styles import GREEN

HELP_MESSAGE = GREEN + '''\n
    -------------------- Help -----------------------------
	Choices for make a operation:
		+ (add)
		- (subtract)
		* (multiply)
		/ (divide)

	You must enter two numeric values for make the operation.
    For clean the terminal write c.
    For exit write e.

'''
