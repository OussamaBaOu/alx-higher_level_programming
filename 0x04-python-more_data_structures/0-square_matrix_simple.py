#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix.copy()
    for b in range(len(matrix)):
        a[b] = list(map(lambda x: x**2, matrix[b]))
    return (a)
