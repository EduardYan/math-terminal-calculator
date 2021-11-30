"""
This module have the class Logarithm.
"""

import sys
sys.path.append('..')

from .operation_math import OperationMathematic
from helpers.utils import is_pair
from math import log
from styles.styles import BLACK

class Logarithm(OperationMathematic):
    def __init__(self):
        # initials values
        self.number = None
        self.base = None
        self.type_operation = 'log'

    def get_result(self):
        """
        Return the log.

        10 * x = 12
        x = 12/10

        """

        result_log = log(self.number, self.base)
        return result_log

    def descomp(self):
        """
        Descompone the number
        in primes factories.

        This is the descomposition:
        ---------------------
        12|3
        4|2
        2|2
        1|

        3*2*2 = 12

        ---------------------

        """
        pass


    def __get_divisor(self):
        """
        Return the divisor of the number
        to make the log, between the base.
        """

        # validating for return the divisor
        if self.number % 2 == 0:
            return 2

        elif self.number % 3 == 0:
            return 3

    def show_log(self):
        """
        Show the log result.
        """

        # getting the result and show it
        self.__result = self.get_result()
        print( BLACK + f'\nLogarithm base {self.base} of {self.number} = {self.__result}' )

    def __str__(self):
        return 'This is a logarithm with base {self.base} and number {self.number}.'
