"""
This module have the model class
for create  a mathematic operation
basic.
"""

# this is to get other modules to use
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))

from helpers.utils import define_operator, define_operation_to_make
from options.types_operations import OPERATIONS, OPERATORS, JOIN_OPERATIONS

class OperationMathematic:
    """
    Create a OperationMathematic
    with a n1, n2.

    The property self.operator is None for default.
    And the two values are floats for default.

    This class not support the equation operation and the log operation.
    Each class have yours owns methods.

    """

    def __init__(self, n1, n2):
        # initials values
        self._operator = None
        self._type_operation = None

        # validating the type of data
        if type(n1) not in [int, float]:
            raise TypeError('The parameter n1 not is of type int or float. Must be a int or float.')

        if type(n2) not in [int, float]:
            raise TypeError('The parameter n2 not is of type int or float. Must be a int or float.')

        self._n1 = float(n1)
        self._n2 = float(n2)

    # some interface methods
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        # validating the type of data and the type of operator for change
        if type(value) not in [str]:
            raise TypeError('The value for change the property operator not is a str. Must be a string.')

        # validating the operator value passed for parameter
        if value not in OPERATORS:
            if value not in JOIN_OPERATIONS:
                # solo se va a ejecutar en caso no sea ninguna de las
                # operaciones validas. Esto lo hago para que no falle en la
                # equacion ni en las operaciones basicas
                raise ValueError('The value for define a operator not is a operator valid.')
            else:
                self._operator = define_operator(value, OPERATIONS)

        self._operator = define_operator(value, OPERATIONS)

    @operator.deleter
    def operator(self):
        del self._operator

    @property
    def type_operation(self):
        return self._type_operation

    @type_operation.setter
    def type_operation(self, value):
        if type(value) not in [str]:
            raise TypeError('The value for change the property type_operation not is a str. Must be a string.')

        self._type_operation = define_operation_to_make(value, OPERATIONS)

    @type_operation.deleter
    def type_operation(self):
        del self._type_operation

    @property
    def n1(self):
        return self._n1

    @n1.setter
    def n1(self, value):
        self._n1 = float(value)

    @n1.deleter
    def n1(self):
        del self._n1

    @property
    def n2(self):
        return self._n2

    @n2.setter
    def n2(self, value):
        self._n2 = float(value)

    @n2.deleter
    def n2(self):
        del self._n2


    def get_result_operation(self, operator:str):
        """
        Return the result of the
        operation according to the operator passed by parameter.
        This method validate the type of operation
        for make + - * or / and potency.

        This method not return the result of the operation
        in case be a equation or logarithm, these classes have yours
        owns methods and functionality !!

        """
        # validating the type of data
        if type(operator) not in [str]:
            raise TypeError('The parameter operator not is of type str. Must be a str.')

        # validating for define the operator for use
        self.operator = operator
        # assing the type of the operation
        self.type_operation = self.operator

        # validating for return the result
        if self.operator == '+':
            return self.n1 + self.n2

        if self.operator == '-':
            return self.n1 - self.n2

        if self.operator == '*':
            return self.n1 * self.n2

        if self.operator == '/':
            return self.n1 / self.n2

        if self.operator == '**':
            return self.n1 ** self.n2


    def __str__(self):
        return f'This is a operation of type {self.type_operation}, with first value to {self.n1} and like second value to {self.n2}'
