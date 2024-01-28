#!/usr/bin/python3

''' function to divide a matrix '''
def matrix_divided(matrix, div):
    '''
    define a divided matrix

    Args:
    matrix:matrix to be devided
    div:divisor

    Raises:
    TypeErorr:if matrix not integers or floats
    TypeErorr:if row not the same size
    TypeErorr:if div not a number
    ZerodivisionErorr:if div equal to zero
    
    Return:a new matrix

    '''
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])

    if not all(len(row) == size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[element / div for element in row] for row in matrix]

    return new_matrix
