"""
Test for utils.py
"""

import sys
sys.path.append('..')

import unittest
from helpers.utils import validate_number, isnegative


class TestUtils(unittest.TestCase):
	def setUp(self):
		print('setup')

	def tearDown(self):
		print('tearDown')

	def test_validate_number(self):
		o = validate_number('---123kj4213')
		self.assertEqual(o, True)

	def test_isnegative(self):
		o =  isnegative('12')
		self.assertEqual(o, False)


	"""
	x + value1 =  value2
	x = value2 - value1
	x = v

	x - value1 = value2
	x = value2 + value1
	x = v
	"""


if __name__ == '__main__':
	unittest.main()