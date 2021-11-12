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
    Create a CustomStyle with a color, foregroud, and a style
    """

    # def __init__(self, color:str, foreground:str, style:str):
        # # initial value
        # self.default_color = Fore.LIGHTBLACK_EX + Style.DIM

        # # validating initials values
        # if color is None:
            # self.color = self.default_color

        # self.color = color
        # self.foreground = foreground
        # self.style = style

    def __init__(self, style:dict):
        self.style = style

        if self.validate_option_passed():
            if 'color' in self.style:
                self.color = self.style['color']

            if 'background' in self.style:
                self.background = self.style['background']

            if 'style' in self.style:
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
        # init(autoreset = True)
        # print(self.color + self.foreground + self.style + 'custom style')

        print(self.style)

    def __str__(self):
        # return f'This is a custom style with color {self.color}, foreground {self.foreground} and style {self.style}'
        return 'custom style'

GREEN = CustomStyle( {'color': Fore.GREEN, 'style_text': Style.BRIGHT, 'foreground': Fore.BLACK} )

if __name__ == '__main__':
    print(GREEN)
