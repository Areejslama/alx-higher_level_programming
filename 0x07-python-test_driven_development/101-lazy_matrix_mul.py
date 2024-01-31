#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function takes two arrays as input and
    returns their matrix product.
    The first array must be two-dimensional,
    and the second array can be either two-dimensional or one

     Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    result = np.matmul(m_a, m_b)
    return result
