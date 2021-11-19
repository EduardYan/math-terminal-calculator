"""
This module have the class Subtract.
"""

from .operation_math import OperationMathematic

class Subtract(OperationMathematic):
	"""
	Create a substract with two
	values n1 and n2.
	This class Heredate of OperationMathematic class.

	"""
	def __init__(self, n1, n2):
		super().__init__(n1, n2)
