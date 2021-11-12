"""
This module hava messages
saved in variables for show when the user exit of the
program.
"""

import sys
sys.path.append('..')

from styles.styles import GREEN
from symbols.symbols import FACE

EXIT_MESSAGE = GREEN + '\n' + FACE.symbol_to_show + ' Exited :}'
