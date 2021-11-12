"""
This module have the sytles for show
in the terminal.

Too have the class Style for create the styles.

"""

import sys
sys.path.append('..')

from colorama import Fore, Style, Back, init
from options.styles_options import STYLES_OPTIONS

class CustomStyle:
    """
    Create a CustomStyle with a color, foregroud, and a style.
    This class recibe a style dict object for create the style.

    The keys for put in the dict are:
        {
            'foreground': 'example-color',
            'background': 'example-background',
            'style_text': 'example-style'
        }

    The keys don't necessarily have to be in that order.

    If any of the keys are not in the class options, an exception of
    type TypeError will be thrown.

    """

    def __init__(self, style:dict):
        self.style = style

        if self.validate_option_passed():
            if 'foreground' in self.style:
                self.foreground = self.style['foreground']

            if 'background' in self.style:
                self.background = self.style['background']

            if 'style_text' in self.style:
                self.style_text = self.style['style_text']

    def validate_option_passed(self):
        """
        Return True if the option passed for parameter
        in the constructor is valid.

        """
        # validating the option
        for option in self.style:
            if option not in STYLES_OPTIONS:
                raise TypeError(f'The option {option} passed in the dict, not is a option validate for use.')

        return True

    def imprime_in_console(self):
        """
        Show the custom style create
        in the console.
        """
        print(self.foreground + self.background + self.style_text + 'custom style')

    def get_custom_style(self):
        """
        Return the custom style  created.
        """
        init(autoreset = True)
        return self.foreground + self.background + self.style_text


    def __str__(self):
        # return f'This is a custom style with color {self.color}, foreground {self.foreground} and style {self.style}'
        return 'This is a Custom Style'

GREEN = CustomStyle( {'foreground': Fore.GREEN, 'style_text': Style.DIM, 'background': Back.BLACK} )
GREEN = GREEN.get_custom_style()

YELLOW = CustomStyle( {'foreground': Fore.YELLOW, 'style_text': Style.DIM, 'background': Back.BLACK} )
YELLOW = YELLOW.get_custom_style()

BLUE = CustomStyle( {'foreground': Fore.BLUE, 'style_text': Style.DIM, 'background': Back.BLACK} )
BLUE = BLUE.get_custom_style()

RED = CustomStyle( {'foreground': Fore.RED, 'style_text': Style.DIM, 'background': Back.BLACK} )
RED = RED.get_custom_style()

MAGENTA = CustomStyle( {'foreground': Fore.MAGENTA, 'style_text': Style.DIM, 'background': Back.BLACK} )
MAGENTA = MAGENTA.get_custom_style()

WHITE = CustomStyle( {'foreground': Fore.WHITE, 'style_text': Style.BRIGHT, 'background': Back.BLACK} )
WHITE = WHITE.get_custom_style()


if __name__ == '__main__':
    print(GREEN)
