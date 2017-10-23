# -*- coding: utf-8 -*-
"""
    二维数组中的查找
    ~~~~~~~~~~~~~~~
    题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
    照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
    整数，判断数组中是否含有该整数。
"""


def search_in_sorted_matrix(matrix, target):
    if not matrix:
        return False
    rows, columns = len(matrix), len(matrix[0])
    r, c = 0, columns - 1
    while r < rows and c >= 0:
        if matrix[r][c] > target:
            c -= 1
        elif matrix[r][c] < target:
            r += 1
        else:
            return True
    return False


if __name__ == '__main__':
    matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    rv = search_in_sorted_matrix(matrix, 7)
    print(rv)
