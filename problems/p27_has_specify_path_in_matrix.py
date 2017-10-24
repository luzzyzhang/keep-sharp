# -*- coding: utf-8 -*-
"""
    矩阵中的路径
    ~~~~~~~~~~~~
    题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
    字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
    上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
    该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
    母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
    字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
"""


def has_path_in_matrix(matrix, path):
    if not matrix or not path:
        return False
    rows, cols = len(matrix), len(matrix[0])
    index = 0
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if has_path(matrix, r, c, path, index, visited):
                return True
    return False


def has_path(matrix, row, col, path, index, visited):
    rows, cols = len(matrix), len(matrix[0])
    if index == len(path):
        return True
    in_path = False
    if ((row >= 0 and row < rows) and (col >= 0 and col < cols)
            and (matrix[row][col] == path[index])
            and (not visited[row][col])):
        index += 1
        visited[row][col] = 1
        left = has_path(matrix, row, col-1, path, index, visited)
        right = has_path(matrix, row, col+1, path, index, visited)
        up = has_path(matrix, row-1, col, path, index, visited)
        down = has_path(matrix, row+1, col, path, index, visited)
        in_path = left or right or up or down
        if not in_path:
            index -= 1
            visited[row][col] = 0
    return in_path


if __name__ == '__main__':
    matrix = [['a', 'b', 't', 'g'],
              ['c', 'f', 'c', 's'],
              ['j', 'd', 'e', 'h']]
    path = 'bfce'
    path2 = 'abfb'
    r = has_path_in_matrix(matrix, path)
    r2 = has_path_in_matrix(matrix, path2)
    print(r, r2)
