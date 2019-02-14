"""
This is a test for do the animation
"""

def make_animation():
	from time import sleep

	point = '.'

	# showign each element
	print('Login ', end = '')

	for i in range(4):
		print( point, end = '' )

		# waiting
		sleep(0.5)

make_animation()