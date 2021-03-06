"""
This module have the symbols for show
in the process of the operations.
Created with the Symbol class.

"""


class Symbol:
    """
    Create a Symbol with the symbol
    in unicode and the symbole for show in the console.

    """

    def __init__(self, code_unicode:str, symbol_to_show:str):
        # properties
        self.code_unicode = code_unicode
        self.symbol_to_show = symbol_to_show

    def imprime_in_console(self):
        """
        Show in console the self.symbol_to_show property.
        """

        print(self.symbol_to_show)

    def __str__(self):
        return self.symbol_to_show


# theses are for the check marks
CHECK1 = Symbol('\u2705', '✅')
CHECK2 = Symbol('\u2713', '✓')
CHECK3 = Symbol('\u2714', '✔')
CHECK4 = Symbol('\u1F5F8', '🗸')

# these are for the x marks
BADCHECK1 = Symbol('\u274C', '❌')
BADCHECK2 = Symbol('\u274E', '❎')
BADCHECK3 = Symbol('\u2718', '✘')

# this is for the help
HELP_CIRCULE = Symbol(None, '🛈')

# some others marks
FACE = Symbol('\u1F60E', '😎')

if __name__ == '__main__':
    print('testing the symbols for show')

    print(CHECK1)
    print(CHECK2)
    print(CHECK3)
    print(CHECK4)
    print(BADCHECK1)
    print(BADCHECK2)
    print(BADCHECK3)
    print(FACE)
    print(HELP_CIRCULE)
