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
from options.help_options import HELP_OPTIONS
from helpers.utils import show_operations_maked
from login import login


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
        # definning the operation to make and the type of operation
        user.operation_to_make = type_operation
        print( f'The operation to make is {user.operation_to_make}.' )

        # validating for exit of the program
        if type_operation == OPTIONS[0] or type_operation == OPTIONS[1] or type_operation == OPTIONS[2] or type_operation == OPTIONS[3] or type_operation == OPTIONS[4] or type_operation == OPTIONS[5] or type_operation == OPTIONS[6]:
            break

        # in case the type of operation no be supported, validating
        elif type_operation not in JOIN_OPERATIONS + HELP_OPTIONS:
            print( OPERATION_UNKNOW )

        # for get help
        elif type_operation == 'help':
            print( HELP_MESSAGE )

        else:
            # the user making the operation
            user.make_operation(type_operation)
            show_operations_maked(user)

    # for when exit of the while loop
    print( EXIT_MESSAGE )


if __name__ == '__main__':
    main()