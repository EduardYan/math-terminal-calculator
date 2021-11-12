"""
This is a test for do some functionaly
in the program.
"""

import sys
sys.path.append('..')

from symbols.symbols import CHECK4

def e6():
    from time import sleep
    from colorama import Cursor, Fore

    print('moviendo figura a una posicion ...')
    for progress in ['']:
        sleep(0.5)
        print(Cursor.POS(37, 6) + Fore.LIGHTYELLOW_EX + str(progress))
    print(Cursor.POS(37, 10) + Fore.LIGHTYELLOW_EX + 'Ya termino ...')


def make_animation():
    """
    Make a animation  for show in the login
    processing.
    """
    from time import sleep
    from colorama import Cursor, Fore, init

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
    for i in range(1, len(list_points)):
        if i < 6:
            print( Cursor.POS(50, 6) + Fore.BLUE + list_points[i] + f' {i}' )
        else:
            print( Cursor.POS(50, 6) + Fore.BLUE + list_points[i] + f' {i - 1} ' + CHECK4.symbol_to_show )
        sleep(0.5)

if __name__ == '__main__':
    print('This is a test. Jeje.')
