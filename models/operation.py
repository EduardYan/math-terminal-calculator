"""
This module have a class Operation
for use in the program.

"""

from .operations.add import Add
from .operations.subtract import Subtract
from .operations.multiply import Multiply
from .operations.divide import Divide
from .operations.potency import Potency
from .operation.pontecy import Ecuation
from helpers.utils import validate_number, define_operation_to_make
from options.types_operations import OPERATIONS
from messages.error_messages import VALUE_ERROR, ZERO_ERROR, SYNTAX_ERROR
from styles.styles import MAGENTA, GREEN, RED


class Operation:
    """
    Create a object type Operation
    recived like parameter the type of operation
    for make.

    The values can be:
        '+', '-', '*' or '/'

    Depending of the type of operation
    the constructor method, generate two inputs
    for get the first number and the second number for make the operation.

    In alls the functions instance a class for the operation to make, and return
    the value of the each class. Also controlling some exception of error with a block
    try except.

    See operations classes in ./operations/

    """

    def __init__(self, type_operation):
        # Validating the type of data
        if type(type_operation) not in [str]:
            raise TypeError('The parameter type not is a string valid.')

        # initials values
        self.type = type_operation
        self.n1 = None
        self.n2 = None

        # this validation is for define the name of the operation to make
        self.name_operation = define_operation_to_make(type_operation, OPERATIONS)


    def make_operation(self):
        """
        Make the operation, getting the two
        values and print the output.
        """

        # validating the type of operation for make
        if self.type in OPERATIONS[0]:
            # in case is add operation, showing the inputs
            self.__show_inputs_basics()

            # validating if the value of the numbers is numeric
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            else:
                result = self.__get_result_add()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation) )

        if self.type in OPERATIONS[1]:
            # in case is subtract operation, showing the inputs
            self.__show_inputs_basics()

            # validating if the value of the numbers is numeric
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            else:
                result = self.__get_result_substract()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation) )

        if self.type in OPERATIONS[2]:
            # in case is multiply operation, showing the inputs
            self.__show_inputs_basics()

            # validating if the value of the numbers is numeric
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            else:
                result = self.__get_result_multiply()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation))

        if self.type in OPERATIONS[3]:
            # in case is divide operation, showing the inputs
            self.__show_inputs_basics()

            # validating if the value of the numbers are numeric values
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            # in case be cero
            elif self.n2 == '0':
                print( ZERO_ERROR )

            else:
                result = self.__get_result_divide()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation) )

        if self.type in OPERATIONS[4]:
            # in case is divide operation, showing the inputs
            self.__show_inputs_pontency()

            # validating if the value of the numbers are numeric values
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            else:
                result = self.__get_result_potency()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation) )

        if self.type in OPERATIONS[5]:
            # in case is divide operation, showing the inputs
            self.__show_inputs_pontency()

            # validating if the value of the numbers are numeric values
            if not validate_number(self.n1):
                print( VALUE_ERROR.format(number = 1, number_value = self.n1) )

            elif not validate_number(self.n2):
                print( VALUE_ERROR.format(number = 2, number_value = self.n2) )

            else:
                result = self.__get_result_potency()
                print( GREEN + f'Output > {result}' ) if not result == 'e' else print( SYNTAX_ERROR.format(name_operation = self.name_operation) )


    def get_operation(self):
        """
        Only return the self.type property for use.
        """
        return self.type

    def __show_inputs_basics(self):
        """
        Show two inputs for get
        the first number and the second.
        Return the 2 values.
        """

        # assing the new value to the properties for make the operation
        self.n1, self.n2 = input( MAGENTA + '\nNumber 1: '), input( MAGENTA + 'Number 2: ')

    def __show_inputs_pontency(self):
        """
        Show two inputs for get the ... doc here -----------
        """
        self.n1, self.n2 = input( MAGENTA + '\nNumber to Pontecy: '), input( MAGENTA + 'Pontency: ')


    def __show_inputs_ecuation(self):
        """
        Show two inputs for get the variable, the value one
        and the value two for make the equation and find the variable
        """
        # self.n1, self.n2, self.variable = input( MAGENTA + '\n:'), input( MAGENTA + 'Pontency: ')
        # ggooooooooooooooooooooooooooooooo

    def __get_result_add(self):
        """
        Return the result of the operation created
        in case be a add.
        """
        try: # this is in case happend in syntax error of whatever type
            add = Add( float(self.n1), float(self.n2) )
            total = add.get_result_operation(self.type)
            return total

        except:
            return 'e'

    def __get_result_substract(self):
        """
        Return the result of the
        opearation created, in case be a subtract.
        """
        try:
            substract = Subtract( float(self.n1),  float(self.n2) )
            total = substract.get_result_operation(self.type)
            return total

        except:
            return 'e'

    def __get_result_multiply(self):
        """
        Return the result of the operation
        created, in case be a multiply
        """
        try:
            multiply = Multiply( float(self.n1), float(self.n2) )
            total = multiply.get_result_operation(self.type)
            return total

        except:
            return 'e'

    def __get_result_divide(self):
        """
        Return the result of the operation
        create, in case be a divide
        """
        try:
            divide = Divide( float(self.n1), float(self.n2) )
            total = divide.get_result_operation(self.type)
            return total
        except:
            return 'e'

    def __get_result_potency(self):
        """
        Return the result of the operation
        created , in case be a pontecy.
        """
        try:
            pontecy = Potency( int(self.n1), int(self.n2) )
            total = pontecy.get_result_operation(self.type)
            return total
        except:
            return 'e'

    def __get_result_ecuation(self):
        """
        Return the result of the
        opeartion created in case be a ecuation
        """
        # try:
        #     ecuation = Ecuation( int(self.n1), int(self.n2) )
        #     total = ecuation.get_result_ecuation(self.type)
        #     return total
        # except:
        #     return 'e'
        ecuation = Ecuation( float(self.n1), float(self.n2) )
        ecuation.get_result_operation()


    def __str__(self):
        return 'The type of the operation is {self.type}.'
