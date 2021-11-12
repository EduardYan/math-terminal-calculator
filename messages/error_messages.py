"""
This module have messages saved
in variables for show in error case to user.
"""

import sys
sys.path.append('..')

from styles.styles import RED
from symbols.symbols import BADCHECK3

# in case not put a operation
OPERATION_UNKNOW = RED + BADCHECK3.symbol_to_show + ' Choice some operation for make (+, -, *, /).'

# in case a operational error
VALUE_ERROR = RED + BADCHECK3.symbol_to_show + ' The value of number {number} {number_value} not is a number. Enter a numeric value.'
ZERO_ERROR = RED + BADCHECK3.symbol_to_show + " The number 2 is a 0. Can't divide between zero."

# in case happend a syntax error
SYNTAX_ERROR = RED + BADCHECK3.symbol_to_show + ' Syntax error for make the operation {name_operation}. Try again.'
