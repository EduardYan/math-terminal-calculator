"""
This module have messages for show
help to user
"""

import sys
sys.path.append('..')

from styles.styles import GREEN
from symbols.symbols import HELP_CIRCULE

HELP_MESSAGE = GREEN + f'''\n
    -------------------- Help {HELP_CIRCULE} -----------------------------
    Choices for make a operation:
        + (add)
        - (subtract)
        * (multiply)
        / (divide)
        po (potency)
        ec (make a simple ecuation)

	You must enter two numeric values for make the operation.
    For clean the terminal write c.
    For exit write e.

'''
