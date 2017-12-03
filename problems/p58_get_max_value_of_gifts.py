# -*- coding: utf-8 -*-
"""
    礼物的最大价值
    ~~~~~~~~~~~~~~
    在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
    （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或
    者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
    算你最多能拿到多少价值的礼物？
"""


def max_value(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_values = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            left, up = 0, 0
            if r > 0:
                up = max_values[r-1][c]
            if c > 0:
                left = max_values[r][c-1]
            max_values[r][c] = max(left, up) + matrix[r][c]
    max_value = max_values[rows-1][cols-1]
    return max_value


def max_value2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_values = [0 for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            left, up = 0, 0
            if r > 0:
                up = max_values[c]
            if c > 0:
                left = max_values[c-1]
            max_values[c] = max(left, up) + matrix[r][c]
    max_value = max_values[cols-1]
    return max_value


if __name__ == '__main__':
    matrix = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]
    ]
    expect = 53
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expect2 = 29
    rv = max_value2(matrix)
    rv2 = max_value(matrix2)
    assert rv == expect, 'Output=>{}'.format(rv)
    assert rv2 == expect2, 'Output=>{}'.format(rv)
