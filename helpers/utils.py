"""
This module have some functions
for do functionalities utils of the program.

Show data of the operations, etc ...
"""

import sys
sys.path.append('..') # this is for can get other modules for use

from options.types_operations import OPERATIONS

def show_operations_maked(user:object):
    """
    Show the numbers of operations
    maked for the user.

    Recive the user that is playing.
    """

    # getting the number
    maked = user.get_operations_maked()
    print(f'\n<== {user.username} you have maked {maked} operations ==>')


def validate_number(number:str):
    """
    Validate if the number is valid
    for make the operation
    """
    # getting the list of negatives signes
    options = OPERATIONS[1]

    # validating if in the options
    if number[0] in options:
        return True
    if number[0].isdigit():
        return True

    return False

def define_operation_to_make(property:str, operations_list:list):
    """
    Return the type of operation to make.
    Validating the operations list defined.
    """

    # validating for define the property of the object
    if property in operations_list[0]:
        property = 'Add'

    if property in operations_list[1]:
        property = 'Subtract'

    if property in operations_list[2]:
        property = 'Multiply'

    if property in operations_list[3]:
        property = 'Divide'

    if property in operations_list[4]:
        property = 'Potency'

    if property in operations_list[5]:
        property = 'Ecuation'

    if property in operations_list[6]:
        property = 'Logarithm'

    return property

def define_operator(property:str, operations_list:list):
    """
    Return the type of operator depending of the operations_list
    passed for parameter.
    """

    if property in OPERATIONS[0]:
        property = '+'

    if property in OPERATIONS[1]:
        property = '-'

    if property in OPERATIONS[2]:
        property = '*'

    if property in OPERATIONS[3]:
        property = '/'

    if property in OPERATIONS[4]:
        property = '**'

    if property in OPERATIONS[5]:
        property = 'ec'

    return property


def clear_terminal():
    """
    This function clean the
    information in the terminal for the user.
    """
    import os

    # validating the os system
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')


def isnegative(number:str):
    """
    Return True if the number is negative.
    If the number is positive return False.
    """
    # validating the number

    return True if number[0] == '-' else False


def is_pair(number:float):
    """
    Return True if the number passed for parameter
    is pair.
    """
    # validating and returning
    return True if number % 2 == 0 else False
