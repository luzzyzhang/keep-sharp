# -*- coding: utf-8 -*-
"""
    最小的k个数
    ~~~~~~~~~~
    输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
    这8个数字，则最小的4个数字是1、2、3、4。
"""

# import heapq

from util import partition


def get_least(numbers, k):
    if not numbers:
        return []
    start, end = 0, len(numbers) - 1
    index = partition(numbers, start, end)
    while index != k-1:
        if index > k-1:
            end = index-1
            index = partition(numbers, start, end)
        else:
            start = index+1
            index = partition(numbers, start, end)
    print(numbers)
    return numbers[:k]


if __name__ == '__main__':
    numbers = [4, 5, 1, 6, 2, 7, 3, 8]
    expect = [1, 2, 3, 4]
    assert get_least(numbers, 4) == expect
