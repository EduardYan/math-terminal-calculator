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
LOG = ['log', 'log ', 'log  ', 'log   ', 'log    ', 'log     ']

# this is a tuple with the list of operations
OPERATIONS = (ADD, SUBTRACT, MULTIPLY, DIVIDE, POTENCY, ECUATION, LOG)

# this is a list with the operations join
JOIN_OPERATIONS = ADD + SUBTRACT + MULTIPLY + DIVIDE + POTENCY + ECUATION + LOG

# this is for validate the operators with a list
OPERATORS = ADD + SUBTRACT + MULTIPLY + DIVIDE
