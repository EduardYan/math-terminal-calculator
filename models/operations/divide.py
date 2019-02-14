"""
This module have the class Divide for use.
"""

class Divide:
	"""
	Create a Divide with two values
	n1 and n2.
	"""

	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2

	def get_total(self):
		"""
		Return the divide between the
		self.n1 and self.n2.
		"""
		total = self.n1 / self.n2
		return total

	def __str__(self):
		return 'This Divide have like first value to {self.n1}, and like second value to {self.n2}.'