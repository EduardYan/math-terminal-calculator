"""
This is the principal file for execute
the terminal program.
"""

from messages.initial_messages import INITIAL_MESSAGE
from messages.exit_messages import EXIT_MESSAGE
from messages.help_messages import HELP_MESSAGE
from messages.error_messages import OPERATION_UNKNOW
from options.exit_options import OPTIONS
from options.types_operations import JOIN_OPERATIONS
from login import login
from models.operation import Operation

def show_operations_maked(user):
	"""
	Show the numbers of operations
	maked for the user.
	
	Recive the user that is playing.
	"""

	# getting the number
	maked = user.get_operations_maked()
	print(f'\n{user.username} you have maked {maked} operations.')


def main():
	"""
	This is the principal function for execute.
	"""	
	
	# Getting the username
	user = login()

	# Showing initial messages
	print( INITIAL_MESSAGE.format(username = user.username) )

	# PRINCIPAL LOOP
	while True:
		type_operation = input('\nType Operation (+, -, *, /) > ')
		print( f'The operation to make is {type_operation}.' )

		# validating for exit of the program
		if type_operation == OPTIONS[0] or type_operation == OPTIONS[1] or type_operation == OPTIONS[2] or type_operation == OPTIONS[3] or type_operation == OPTIONS[4] or type_operation == OPTIONS[5] or type_operation == OPTIONS[6]:
			break

		# in case the type of operation no be supported, validating
		elif type_operation not in JOIN_OPERATIONS:
			print( OPERATION_UNKNOW )

		# for get help
		elif type_operation == 'help':
			print( HELP_MESSAGE )

		else:
			# making the operation
			operation = Operation(type_operation)
			operation.make_operation()
			# adding the number
			user.operations_number += 1
			show_operations_maked(user)

	# for when exit of the while loop
	print( EXIT_MESSAGE )


if __name__ == '__main__':
	main()