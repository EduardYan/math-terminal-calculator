"""
This file have the class Error.
"""

import sys
sys.path.append('.')

from styles.styles import RED
from symbols.symbols import BADCHECK3

class ErrorMessage:
    """
    Create a Error with a content
    and the color red for default.
    """

    def __init__(self, content:str, color:str = RED):
        # values initials
        self.content = RED + BADCHECK3.symbol_to_show + content
        self.color = color

    def __str__(self):
        return f'This is a error: {self.content}'
