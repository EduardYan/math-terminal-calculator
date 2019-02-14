"""
Test for utils.py
"""

import sys
sys.path.append('..')

import unittest
from helpers.utils import validate_number, isnegative


class TestUtils(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_validate_number(self):
        print('Test validate_number function')

        o = validate_number('---123kj4213')
        self.assertEqual(o, True)

        self.assertEqual(validate_number('2341'), True)


    def test_isnegative(self):
        """
        x + value1 =  value2
        x = value2 - value1
        x = v

        x - value1 = value2
        x = value2 + value1
        x = v
        """

        print('Test is_negative function')

        o =  isnegative('12')
        self.assertEqual(o, False)


if __name__ == '__main__':
    unittest.main()
