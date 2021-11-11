"""
This module have the class Add.
"""

import sys
import os
# this is to get other modules to use
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir + '/operations/')))

from operation_math import OperationMathematic

class Add(OperationMathematic):
	"""
	Create a add with a n1 and a n2 values.
	This class heredate of OperationMath class.

	"""
	def __init__(self, n1, n2):
		super().__init__(n1, n2)