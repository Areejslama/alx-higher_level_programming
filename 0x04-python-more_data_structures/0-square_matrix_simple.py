#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in matrix:
        squared_raw = list(map(lambda row: row**2, i))
        squared_matrix.append(squared_raw)
    return squared_matrix
