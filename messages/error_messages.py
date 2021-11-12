"""
This module have messages saved
in variables for show in error case to user.
"""

import sys
sys.path.append('..')

from styles.styles import RED

# in case not put a operation
OPERATION_UNKNOW = RED + 'Choice some operation for make (+, -, *, /).'

# in case a operational error
VALUE_ERROR = RED + 'The value of number {number} {number_value} not is a number. Enter a numeric value.'
ZERO_ERROR = RED + "The number 2 is a 0. Can't divide between zero."

# in case happend a syntax error
SYNTAX_ERROR = RED + 'Syntax error for make the operation {name_operation}. Try again.'
