from copy import deepcopy
import numpy as np


# Questão 1
def reverse_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    return_matrix = deepcopy(matrix)
    for i, item in enumerate(matrix):
        for j, item_2 in enumerate(item):
            if i == j:
                index = len(item) - (i + 1)
                return_matrix[index][index] = item_2
            elif i + j == (len(matrix) - 1):
                return_matrix[j][i] = item_2
    return return_matrix


# Questão 2
def count_repeat_matrix(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> int:
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    rows_matrix_a, cols_matrix_a = matrix_a.shape
    rows_matrix_b, cols_matrix_b = matrix_b.shape
    count = 0
    for i in range(rows_matrix_a - rows_matrix_b + 1):
        for j in range(cols_matrix_a - cols_matrix_b + 1):
            sub_matrix = matrix_a[i : i + rows_matrix_b, j : j + cols_matrix_b]
            if np.all(matrix_b.__eq__(sub_matrix)):
                count += 1

    return count


if "__main__":
    # Questão 1
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(reverse_diagonal(matrix))

    # Questão 2
    matrix_b = [[1, 2], [5, 6]]
    print(count_repeat_matrix(matrix, matrix_b))
