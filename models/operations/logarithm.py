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

        This is the descomposition:
        ---------------------
        12|3
        4|2
        2|2
        1|

        3*2*2 = 12

        ---------------------

        """

        # validating if the number is pair or inpair for return the number
        if is_pair(self.number):
            # import pdb; pdb.set_trace() # for debug

            divisor = self.__get_divisor(self.number)

            div = self.number / divisor # dividing
            count = 1 # counter for know the count of the while loop

            while div != 1:
                print(div)

                div = div / divisor
                count += 1

            print(div)
            return count

        else:
            print('the number not is pair')


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
        print('showing the log')

    def __str__(self):
        return 'This is a logarithm'
