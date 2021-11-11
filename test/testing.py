"""
This is a test for do the animation
"""

# from time import sleep

# point = '.'

# for i in range(4):
# 	print(point)
# 	sleep(0.5)
# print(point, end = '')

def e6():
   from time import sleep
   from colorama import Cursor, init, Fore

   print('moviendo figura a una posicion ...')
   for progress in ['.', '..', '..']:
      sleep(1)
      print(Cursor.POS(37, 3) + Fore.LIGHTYELLOW_EX + str(progress))
   print(Cursor.POS() + Fore.LIGHTYELLOW_EX + 'Ya termino ...')

if __name__ == '__main__':
	pass