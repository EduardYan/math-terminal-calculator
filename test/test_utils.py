"""
Test for utils.py
"""

import sys
sys.path.append('/home/pi/Personal_dan/Python-Proyects/math-terminal-calculator/')

import unittest
from helpers.utils import validate_number


class TestUtils(unittest.TestCase):
	def setUp(self):
		print('setup')

	def tearDown(self):
		print('tearDown')

	def test_validate_number(self):
		o = validate_number('---123kj4213')
		self.assertEqual(o, True)


if __name__ == '__main__':
	unittest.main()