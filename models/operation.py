"""
This module have a class Operation
for use in the program.
"""

from options.types_operations import OPERATIONS
from models.add import Add
from models.subtract import Subtract
from models.multiply import Multiply
from models.divide import Divide

class Operation:
	"""
	Create a object type Operation
	recived like parameter the type of operation
	for make.

	The values can be:
		'+', '-', '*' or '/'

	Depending of the type of operation
	the constructor method, generate two inputs
	for get the first number and the second number for make the operation.
	"""

	def __init__(self, type_operation):
		# Validating the type of data
		if type(type_operation) not in [str]:
			raise TypeError('The parameter type not is a string valid.')

		# initials values
		self.type = type_operation
		self.n1 = None
		self.n2 = None

	def make_operation(self):
		"""
		Make the operation, getting the two
		values and print the output.
		"""

		# validating the type of operation
		if self.type in OPERATIONS[0]:
			# in case is add operation, showing the inputs
			self.__show_inputs()

			# validating if the value of the numbers is numeric
			if self.n1.isdigit() == False:
				print(f'The value of number 1 {self.n1} not is a nubmer. Enter a numeric value.')

			elif self.n2.isdigit() == False:
				print(f'The value of the number 2 {self.n2} not is a number. Enter a numeric value.')
					
			else:
				result = self.__get_result_add()
				print( f'Output > {result}' )

		if self.type in OPERATIONS[1]:
			# in case is subtract operation, showing the inputs
			self.__show_inputs()

			# validating if the value of the numbers is numeric
			if self.n1.isdigit() == False:
				print(f'The value of number 1 {self.n1} not is a nubmer. Enter a numeric value.')

			elif self.n2.isdigit() == False:
				print(f'The value of the number 2 {self.n2} not is a number. Enter a numeric value.')
					
			else:
				result = self.__get_result_substract()
				print( f'Output > {result}' )

		if self.type in OPERATIONS[2]:
			# in case is multiply operation, showing the inputs
			self.__show_inputs()

			# validating if the value of the numbers is numeric
			if self.n1.isdigit() == False:
				print(f'The value of number 1 {self.n1} not is a nubmer. Enter a numeric value.')

			elif self.n2.isdigit() == False:
				print(f'The value of the number 2 {self.n2} not is a number. Enter a numeric value.')
					
			else:
				result = self.__get_result_multiply()
				print( f'Output > {result}' )
		
		if self.type in OPERATIONS[3]:
			# in case is divide operation, showing the inputs
			self.__show_inputs()

			# validating if the value of the numbers is numeric
			if self.n1.isdigit() == False:
				print(f'The value of number 1 {self.n1} not is a nubmer. Enter a numeric value.')

			elif self.n2.isdigit() == False:
				print(f'The value of the number 2 {self.n2} not is a number. Enter a numeric value.')
				
			# in case be cero
			elif self.n2 == '0':
				print("The number 2 is a 0. Can't divide between cero.")

			else:
				result = self.__get_result_divide()
				print( f'Output > {result}' )
		

	def get_operation(self):
		"""
		Only return the self.type property.
		"""
		return self.type

	def __show_inputs(self):
		"""
		Show two inputs for get
		the first number and the second.
		Return the 2 values.
		"""

		# assing the new value to the properties
		self.n1, self.n2 = input('\nNumber 1: '), input('Number 2: ')

	def __get_result_add(self):
		"""
		Return the result of the operation created
		in case be a add.
		"""
		add = Add( float(self.n1), float(self.n2) )
		total = add.get_total()
		return total

	def __get_result_substract(self):
		"""
		Return the result of the
		opearation created, in case be a subtract.
		"""
		substract = Subtract( float(self.n1),  float(self.n2) )
		total = substract.get_total()
		return total

	def __get_result_multiply(self):
		"""
		Return the result of the operation
		created, in case be a multiply
		"""
		multiply = Multiply( float(self.n1), float(self.n2) )
		total = multiply.get_total()
		return total

	def __get_result_divide(self):
		"""
		Return the result of the operation
		create, in case be a divide
		"""
		divide = Divide( float(self.n1), float(self.n2) )
		total = divide.get_total()
		return total

	def __str__(self):
		return 'The type of the operation is {self.type}.'