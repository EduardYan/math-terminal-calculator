"""
This module have messages saved
in variables for show in error case to user.
"""

import sys
sys.path.append('.')

from models.error import ErrorMessage

# in case not put a operation
OPERATION_UNKNOW = ErrorMessage(' Choice some operation for make (+, -, *, /).')
OPERATION_UNKNOW = OPERATION_UNKNOW.content

# in case a operational error
VALUE_ERROR = ErrorMessage(' The value of number {number} {number_value} not is a number. Enter a numeric value.')
VALUE_ERROR = VALUE_ERROR.content

# in case error of zero
ZERO_ERROR = ErrorMessage(" The number 2 is a 0. Can't divide between zero.")
ZERO_ERROR = ZERO_ERROR.content

# in case happend a syntax error
SYNTAX_ERROR = ErrorMessage(' Syntax error for make the operation {name_operation}. Try again.')
SYNTAX_ERROR = SYNTAX_ERROR.content

# in case the operator of the equation not be valid
OPERATOR_EQUATION_ERROR = ErrorMessage(' The operator of the equation not is valid. Choice some operator (+, -, * or /).')
OPERATOR_EQUATION_ERROR = OPERATOR_EQUATION_ERROR.content
