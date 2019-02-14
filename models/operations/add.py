"""
This module have the class Add.
"""

class Add:
	"""
	Create a add with a n1 and a n2 values.

	"""
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2

	def get_total(self):
		"""
		Return the add between the
		self.n1 and the self.n2
		"""
		return self.n1 + self.n2

	def __str__(self):
		return 'This Add have like first value to {self.n1}, and like second value to {self.n2}.'