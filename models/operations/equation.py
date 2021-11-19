"""
This module have the class
Equation for make  a equation
"""

import sys
sys.path.append('..')

from messages.equation_messages import HELP_EQUATION_MESSAGE
from .operation_math import OperationMathematic
from helpers.utils import isnegative
from styles.styles import GREEN, BLACK, MAGENTA

class Equation(OperationMathematic):
	"""
	Create a equation with a variable
	for find your value, and two
	numbers to find the variable of the equation.
	"""
	def __init__(self):
		# initials values
		self.variable_to_find = 'x'

	def show_inputs_equation(self):
		"""
		Show two inputs for get the value1, the value2
		and the operator for make equation.
		"""
		# getting the values and adding this properties at the father class
		self.n1 = float(input( MAGENTA + 'Value 1: ') )
		self.operator = input( MAGENTA + 'Operator: ')
		self.n2 = float(input( MAGENTA + 'Value 2: ') )

	def show_help_equation(self):
		"""
		Show information about the equation to make.
		"""
		print(HELP_EQUATION_MESSAGE)

	def __show_equation_maked(self):
		"""
		Show the equation maked for the user
		with the values and the variable.
		"""
		print( BLACK + f'\nEquation maked:  {self.variable_to_find} {self.operator} {self.n1} = {self.n2}' )

	def transpons_terms(self):
		"""
		Transpons the terms of the equation.
		"""

		# validating if is negative (here is the algoritm)
		if self.operator == '-':
			if isnegative(str(self.n1)) and isnegative(str(self.n2)):
				return self.n2 + self.n1

			if not isnegative(str(self.n1)) and not isnegative(str(self.n2)):
				return self.n2 + self.n1

			return self.n2 - self.n1
		else:
			if isnegative(str(self.n1)) and isnegative(str(self.n2)):
				return self.n2 + self.n1

			return self.n2 - self.n1

	def get_result_equation(self):
		"""
		Return the result of the equation, executing
		the encapsulate method __transpons_terms.
		"""
		return self.transpons_terms()

	def show_result_equation(self):
		"""
		Return the result of the ecuation.
		Returning the value of the variable to find.
		"""

		# showing the equation maked
		self.__show_equation_maked()

		result = self.transpons_terms() # getting the result
		print( GREEN + f'The variable x is equal to x = {result}' )
