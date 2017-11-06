# -*- coding: utf-8 -*-
"""
    顺时针打印矩阵
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    ~~~~~~~~~~~~~
    Input:
        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15 16
    Output:
        1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
"""


def print_matrix_clock_wise(matrix):
    rows, columns = len(matrix), len(matrix[0])
    if not matrix or columns <= 0 or rows <= 0:
        return None
    start = 0
    while (columns > start * 2 and rows > start * 2):
        yield from print_matrix_circle(matrix, columns, rows, start)
        start += 1


def print_matrix_circle(matrix, columns, rows, start):
    end_x = columns - 1 - start
    end_y = rows - 1 - start

    # 从左到右打印一行
    for i in range(start, end_x+1):
        number = matrix[start][i]
        yield number

    # 从上到下打印一列
    if start < end_y:
        for j in range(start+1, end_y+1):
            yield matrix[j][end_x]

    # 从右到左打印一行
    if start < end_x and start < end_y:
        for i in range(end_x-1, start-1, -1):
            yield matrix[end_y][i]

    # 从下到上打印一列
    if start < end_x and start < end_y - 1:
        for j in range(end_y-1, start, -1):
            yield matrix[j][start]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expect = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert list(print_matrix_clock_wise(matrix)) == expect
