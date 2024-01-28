#!/usr/bin/python3

''' Define function to add int '''



def add_integer(a, b=98):
    ''' Represents the function
    Args:
    a:an integer to be added
    b:an integer to be added

    Raises:
    TypeError:if a is float
    TypeError:if b is float
    '''
    if not isinstance (a, int) and  not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance (b, int) and not isinstance(b , float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance (b, float):
        b = int(b)

    return(a + b)
