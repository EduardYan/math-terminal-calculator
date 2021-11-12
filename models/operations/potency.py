"""
This module have the class Potency.
"""

from operation_math import OperationMathematic

class Potency(OperationMathematic):
	"""
	Create a Pontency with two values n1 and n2.
	This class heredate of OperationMathematic.
	"""

	def __init__(self, n1, n2):
		super().__init__(n1, n2)
