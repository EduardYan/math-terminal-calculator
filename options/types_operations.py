"""
This module have the types
of the operations for make in the program
"""

# Types of operations
ADD = ['+', '+ ', '+  ', '+   ', '+    ', '+     ']
SUBTRACT = ['-', '- ', '-  ', '-   ', '-    ', '-     ']
MULTIPLY = ['*', '* ', '*  ', '*   ', '*    ', '*     ']
DIVIDE = ['/', '/ ', '/  ', '/   ', '/    ', '/     ']
POTENCY = ['po', 'po ', 'po  ', 'po   ', 'po   ', 'po    ']
ECUATION = ['ec', 'ec ', 'ec  ', 'ec   ', 'ec    ', 'ec    ']

# this is a tuple with the list of operations
OPERATIONS = (ADD, SUBTRACT, MULTIPLY, DIVIDE, POTENCY, ECUATION)

# this is a list with the operations join
JOIN_OPERATIONS = ADD + SUBTRACT + MULTIPLY + DIVIDE + POTENCY + ECUATION