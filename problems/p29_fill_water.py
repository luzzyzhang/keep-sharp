# -*- coding: utf-8 -*-
"""
    Pouring water
    ~~~~~~~~~~~~
    给定 m*n 矩形水槽, 每个格子高度各不相同, 相邻格子可以联通，对角线格子不联通
    现从最左上角格子开始倒水，求一共有多少个格子有水？
    ~~~~~~~~~~~~
    数据结构选择:
    可以使用deque, Queue, but do not use Queue
    https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque
    或者stack用list实现, list.append()和list.pop()最右侧时间复杂度均为O(1)
"""


from collections import deque


def compute_filled_grids(matrix):
    filled = {matrix[0][0]}
    queue = deque([(matrix[0][0], 0, 0)])
    m, n = len(matrix), len(matrix[0])

    while len(queue) != 0:
        current, row, col = queue.popleft()
        right = matrix[row][col+1] if col + 1 < n else float('inf')
        left = matrix[row][col-1] if col - 1 >= 0 else float('inf')
        up = matrix[row-1][col] if row - 1 >= 0 else float('inf')
        down = matrix[row+1][col] if row + 1 < m else float('inf')

        around = ((right, row, col+1), (left, row, col-1),
                  (up, row-1, col), (down, row+1, col))
        for grid, r, c in around:
            if current > grid and grid not in filled:
                filled.add(grid)
                queue.append((grid, r, c))
    return len(filled)


def compute_grids_with_stack(matrix):
    counter = 1
    filled = {matrix[0][0]}
    stack = [(matrix[0][0], 0, 0)]
    m, n = len(matrix), len(matrix[0])

    while len(stack) != 0:
        current, row, col = stack.pop()
        right = matrix[row][col+1] if col + 1 < n else float('inf')
        left = matrix[row][col-1] if col - 1 >= 0 else float('inf')
        up = matrix[row-1][col] if row - 1 >= 0 else float('inf')
        down = matrix[row+1][col] if row + 1 < m else float('inf')

        around = ((right, row, col+1), (left, row, col-1),
                  (up, row-1, col), (down, row+1, col))
        for grid, r, c in around:
            if current > grid and grid not in filled:
                counter += 1
                filled.add(grid)
                stack.append((grid, r, c))
    return counter


if __name__ == '__main__':
    test_matrix1 = [[6, 4, 3], [7, 2, 1], [5, 8, 9]]

    assert compute_filled_grids(test_matrix1) == 5
    assert compute_grids_with_stack(test_matrix1) == 5

    test_matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    assert compute_filled_grids(test_matrix2) == 9
    assert compute_grids_with_stack(test_matrix2) == 9
