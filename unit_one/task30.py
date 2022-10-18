#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

matrix = [[1, 2, 3], [4, 5, 6]]
# msum(matrix)
# 21

def msum(matrix):

    matrix_new = [col for row in matrix for col in row]
    sum_matrix = sum(matrix_new)
    print(sum_matrix)
msum(matrix)