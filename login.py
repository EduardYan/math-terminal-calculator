"""
This file have the function
for make the login of the user.

"""

from time import sleep
from models.user import User

def make_animation():
	"""
	Make a small animation for when the
	user logged
	"""

	print('Login ....')
	sleep(0.5)

	# point = '.'

	# for i in range(4):
	# 	print( point, end = '' )

	# 	# waiting
	# 	sleep(0.5)

	print('\nDone :D' +  '\u2713')
	

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