# -*- coding: utf-8 -*-
"""
    数组中出现次数超过一半的数字
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
    如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
    出现了5次，超过数组长度的一半，因此输出2。
"""

from util import partition


# Approach 1
def more_than_half_num(numbers):
    length = len(numbers)
    middle = length >> 1
    start, end = 0, length-1
    index = partition(numbers, start, end)

    while index != middle:
        if index > middle:
            end = index - 1
            index = partition(numbers, start, end)
        else:
            start = index + 1
            index = partition(numbers, start, end)
    result = numbers[middle]
    if not is_more_than_half(numbers, length, result):
        result = 0
    return result


def is_more_than_half(numbers, length, num):
    times = 0
    for i in range(length):
        if numbers[i] == num:
            times += 1
    return times * 2 > length


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    numbers1 = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    assert more_than_half_num(numbers) == 2
    assert more_than_half_num(numbers1) == 0
