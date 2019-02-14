"""
This module have the class Logarithm.
"""

import sys
sys.path.append('..')

from .operation_math import OperationMathematic
from helpers.utils import is_pair

class Logarithm(OperationMathematic):
    def __init__(self, number, base):
        super().__init__(number, base)
        self.number = number
        self.base = base

    def get_log(self):
        """
        Return the log.

        10 * x = 12
        x = 12/10

        """
        pass

    def descomp(self):
        """
        Descompone the number
        in primes factories.
        """

        # validating if the number is pair or inpair for
        # return the number

        if is_pair(self.number):
            div = self.number / 2
            while div != 1:
                div = div / 2

            return div

        # self.number = self.number / 3
        # while self.number != 1:
            # self.number = self.number / 3

        # return self.number

    def show_log(self):
        """
        Show the log result.
        """
        print('showing the log')
