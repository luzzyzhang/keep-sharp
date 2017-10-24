# -*- coding: utf-8 -*-
"""
    机器人的运动范围
    ~~~~~~~~~~~~~~~~
    题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
    每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
    大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
    但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
"""


def robot_move_count(rows, cols, k):
    if rows <= 0 or cols <= 0 or k < 0:
        return 0
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    count = compute_move_cell(k, rows, cols, 0, 0, visited)
    return count


def compute_move_cell(k, rows, cols, r, c, visited):
    count = 0
    if check_move(k, rows, cols, r, c, visited):
        visited[r][c] = 1

        left = compute_move_cell(k, rows, cols, r, c-1, visited)
        right = compute_move_cell(k, rows, cols, r, c+1, visited)
        up = compute_move_cell(k, rows, cols, r-1, c, visited)
        down = compute_move_cell(k, rows, cols, r+1, c, visited)

        count = 1 + left + right + up + down
    return count


def check_move(k, rows, cols, r, c, visited):
    def digit_sum(number):
        sum_num = 0
        while number > 0:
            sum_num += number % 10
            number //= 10   # 不要使用 number /= 10
        return sum_num

    if ((r >= 0 and r < rows) and
            (c >= 0 and c < cols) and
            (digit_sum(r) + digit_sum(c) <= k) and
            (not visited[r][c])):
        return True
    return False


if __name__ == '__main__':
    assert robot_move_count(10, 10, 5) == 21
    assert robot_move_count(20, 20, 15) == 359
