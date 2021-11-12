"""
This module have the class
Equation for make  a equation
"""


from operation_mathic import OperationMathematic

class Equation(OperationMathematic):
	"""
	Create a equation with a variable
	for find your value, and two
	numbers to find the variable of the equation.
	"""
	def __init__(self, operator, value1, value2):
		super().__init__(value1, value2)
		# initials values
		self.equation_operator = operator
		self.variable = 'x'


	def __transpons_terms(self):
		"""
		Transpons the terms of the equation.
		"""
		print(self.operator, self.n1, self.n2)

	def get_result_ecuation(self):
		"""
		Return the result of the ecuation.
		Returning the value of the variable to find.
		"""
		self.__transpons_terms()