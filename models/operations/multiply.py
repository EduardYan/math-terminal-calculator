"""
This module have the class Multiply for use.
"""

from operation_math import OperationMathematic

class Multiply(OperationMathematic):
	"""
	Create a Multiply with two values
	n1 and n2. This class heredate of OperationMathematic class.
	"""

	def __init__(self, n1, n2):
		super().__init__(n1, n2)