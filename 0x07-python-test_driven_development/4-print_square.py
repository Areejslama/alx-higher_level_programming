#!/usr/bin/python3

''' Define a function '''


def print_square(size):
    ''' represent the function
    Args:
    size: the size of the square

    Raises:
    TypeError: if size is not integer
    ValueError: if size less than 0
    TypeError: if size is float and less than 0

    Return: the square

    '''
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if  isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for n in range(size):
            print('#',  end="")
        print()
