"""
This file have the function
for make the login of the user.

"""

from time import sleep
from colorama import Cursor, Fore, init
from models.user import User
from symbols.symbols import CHECK3, CHECK4


def make_animation():
    """
    Make a animation  for show in the login
    processing.
    """

    # list of points to make a for loop
    list_points = [
        '-----',
        '.----',
        '-.---',
        '--.--',
        '---.-',
        '----.',
        '-----'
    ]

    # this is for that not show others colors
    init(autoreset = True)

    # showing the animation and validating for show the number of progress
    print('Login ....')

    for i in range(1, len(list_points)):
        if i < 6:
            # quiere decir que no ha terminado
            print( Cursor.POS(50, 6) + Fore.BLUE + list_points[i] + f' {i}' )
        else:
            print( Cursor.POS(50, 6) + Fore.BLUE + list_points[i] + f' {i - 1} ' + CHECK4.symbol_to_show )
        sleep(0.5)

    print('\nDone ' +  CHECK3.symbol_to_show)


def login():
	"""
	Make the login for the user
	getting the username.
	Creating a user object.
	"""

	print('Login')

	# getting the username and creating the user object
	username = input('Username > ')
	user = User(username)

	# making the animation
	make_animation()

	# returning the object
	return user

if __name__ == '__main__':
    make_animation()
