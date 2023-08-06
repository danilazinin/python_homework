# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]


def matrix_transpose(matr: list) -> list[list]:
    transpose = list(map(list, zip(*matr)))
    return transpose


print(matrix_transpose(matrix))