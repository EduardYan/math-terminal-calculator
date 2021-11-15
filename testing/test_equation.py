"""
Test equation.py
"""

import sys
sys.path.append('..')

import unittest
from models.operations.equation import Equation

class TestEquation(unittest.TestCase):
	def setUp(self):
		print('setUp')

	def tearDown(self):
		print('tearDown')

	def test_transpons_terms(self):
		e = Equation()
		e.n1 = str(30)
		e.n2 = str(12)
		e.operator = '-'
		o = e.transpons_terms()

		self.assertEqual(o, 42.0)


if __name__ == '__main__':
	unittest.main()