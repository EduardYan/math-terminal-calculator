"""
This module have the class User
for work with the user and use.
"""

class User():
	"""
	Create a User with a name.
	"""

	def __init__(self, name):
		self._username = name
		self._operations_number = 0

	# some interface methods
	@property
	def username(self):
		return self._username
	
	@username.setter
	def username(self, value):
		if type(value) not in [str]:
			raise TypeError('The value for change the property name not is a string. Must be a string')

		self._username = value

	@username.deleter
	def username(self):
		del self._username

	@property
	def operations_number(self):
		return self._operations_number

	@operations_number.setter
	def operations_number(self, value):
		if type(value) not in [int]:
			raise TypeError('The value for change the property operations_number not is a int. Must be a int. ')
			
		self._operations_number = value

	@operations_number.deleter
	def operations_nubmer(self):
		del self._operations_number

	def get_operations_maked(self):
		"""
		Return the number of operations maked 
		with the property self.operations_number
		"""
		return self.operations_number