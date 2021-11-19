"""
This module have the class Add.
"""

from .operation_math import OperationMathematic


class Add(OperationMathematic):
	"""
	Create a add with a n1 and a n2 values.
	This class heredate of OperationMath class.

	"""
	def __init__(self, n1, n2):
		super().__init__(n1, n2)
