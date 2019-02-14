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

        12|2
        6|2
        3|2
        1|1

        2^3


        """

        # validating if the number is pair or inpair for
        # return the number
        if is_pair(self.number):
            div = self.number / 2 # dividing
            count = 1 # counter for know the count of the while loop

            while div != 1:
                div = div / 2
                count += 1

            return count

        else:
            div = self.number / 2
            count = 1

            while div != 1:
                div = div / 2
                count += 1

            return count

    def show_log(self):
        """
        Show the log result.
        """
        print('showing the log')

    def __str__(self):
        return 'This is a logarithm'
