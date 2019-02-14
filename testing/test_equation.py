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
        print('Testing the transpons_terms of the class.')

        e = Equation()
        e.n1 = 30
        e.n2 = 12
        e.operator = '-'
        o = e.transpons_terms()

        self.assertEqual(o, 42.0)

        e2 = Equation()
        e2.n1 = 30
        e2.n2 = 12
        e2.operator = '+'
        o = e2.transpons_terms()


        self.assertEqual(o, -18.0)


if __name__ == '__main__':
    unittest.main()
