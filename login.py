"""
This file have the function
for make the login of the user.
"""

from time import sleep
from models.user import User


def make_animation():
	"""
	Print a animation
	for use in the login function,
	when the user logged.
	"""

	elements_list = ['+', '++', '+++', '++++', '+++++', '++++++']

	# showign each element
	for e in elements_list:
		print(e)
		
		# waiting
		sleep(0.5)



def login():
	"""
	Make the login for the user
	getting the username
	"""
	print('\nLogin')
	# getting the username and creating the user object
	username = input('Username > ')
	user = User(username)

	# login
	print('\nLogin ...')
	# doing the animation
	make_animation()
	print('Done :D')

	# returning the object
	return user