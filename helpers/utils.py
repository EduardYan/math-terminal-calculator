"""
This module have some functions
for do functionalities utils of the program.

Show data of the operations, etc ... 
"""

import sys
sys.path.append('/home/pi/Personal_dan/Python-Proyects/math-terminal-calculator/')

from options.types_operations import SUBTRACT

def show_operations_maked(user):
    """
    Show the numbers of operations
    maked for the user.

    Recive the user that is playing.
    """

    # getting the number
    maked = user.get_operations_maked()
    print(f'\n<== {user.username} you have maked {maked} operations ==>')


def validate_number(number):
	"""
	Validate if the number is valid
	for make the operation
	"""
	options = SUBTRACT

	if number[0] in options:
		return True
	if number[0].isdigit():
		return True

	return False

def define_operation_to_make(property, operations_list):
	"""
	Return the type of operation to make.
	Validating the operations list defined.
	"""

	# validating for define the property of the object
	if property in operations_list[0]:
		property = 'add'

	if property in operations_list[1]:
		property = 'subtract'

	if property in operations_list[2]:
		property = 'multiply'

	if property in operations_list[3]:
		property = 'divide'

	return property