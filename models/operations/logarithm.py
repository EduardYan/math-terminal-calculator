"""
This module have the class Logarithm.
"""

from .operation_math import OperationMathematic


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
        return self.base**(0.4/self.number)

    def show_log(self):
        """
        Show the log result.
        """
        print('showing the log')
