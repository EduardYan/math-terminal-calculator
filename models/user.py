"""
This module have the class User
for work with the user and use.

"""

import sys
sys.path.append('/home/pi/Personal_dan/Python-Proyects/math-terminal-calculator/')

from models.operation import Operation
from helpers.utils import define_operation_to_make
from options.types_operations import OPERATIONS


class User():
    """
    Create a User with a name.
    For make operations.
    """

    def __init__(self, name):
        self._username = name
        self._operations_number = 0
        self._operation_to_make = None

    # some interface methods
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if type(value) not in [str]:
            raise TypeError('The value for change the property name not is a string. Must be a string')

        self._username = value

    @username.deleter
    def username(self):
        del self._username

    @property
    def operations_number(self):
        return self._operations_number

    @operations_number.setter
    def operations_number(self, value):
        if type(value) not in [int]:
            raise TypeError('The value for change the property operations_number not is a int. Must be a int. ')

        self._operations_number = value

    @operations_number.deleter
    def operations_nubmer(self):
        del self._operations_number

    @property
    def operation_to_make(self):
        return self._operation_to_make

    @operation_to_make.setter
    def operation_to_make(self, value):
        if type(value) not in [int, str]:
            raise TypeError('The value for change the property operation_to_make not is a int. Must be a int.')

        self._operation_to_make = define_operation_to_make(value, OPERATIONS)

    @operation_to_make.deleter
    def operation_to_make(self):
        del self._operation_to_make
    

    def make_operation(self, type_operation):
        """
        Make a operation with the Operation class.
        """

        # making the operation
        operation = Operation(type_operation)
        operation.make_operation()

        # adding the number of operations
        self.operations_number += 1


    def get_operations_maked(self):
        """
        Return the number of operations maked
        with the property self.operations_number
        """
        return self.operations_number
