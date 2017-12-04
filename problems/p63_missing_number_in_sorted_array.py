# -*- coding: utf-8 -*-
"""
    0到n-1中缺失的数字
    ~~~~~~~~~~~~~~~~~
    一个长度为n-1的`递增排序数组`中的所有数字都是唯一的，
    并且每个数字都在范围0到n-1之内。
    在范围0到n-1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""


# 直观方法O(n)算法复杂度(求和算法复杂度O(n))
def get_missing_number(array):
    n = len(array) + 1
    return n*(n-1) // 2 - sum(array)


# 递增排序数组 --> 使用二分查找
# array = [0, 1, 2, 4, 5], 数组长度5，n=6
# index = [0, 1, 2, 3, 4], 对应的索引
# 找出第一个值和下标不相等的元素
def get_missing_number_by_binary_search(array):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        if array[middle] != middle:
            if middle == 0 or array[middle-1] == middle-1:
                return middle
            right = middle - 1
        else:
            left = middle + 1

    return left if (left == len(array)) else -1


if __name__ == '__main__':
    array = [0, 1, 2, 4, 5]
    expect = 3
    rv = get_missing_number(array)
    rv2 = get_missing_number_by_binary_search(array)
    assert rv == expect, 'Invalid result {}'.format(rv)
    assert rv2 == expect, 'Invalid result {}'.format(rv2)
