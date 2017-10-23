# -*- coding: utf-8 -*-
"""
    不修改数组找出重复元素
    ~~~~~~~~~~~~~~~~~~~~~
    在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
    少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
    数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
    输出是重复的数字2或者3。
"""


def find_duplications(numbers):
    start, end = 1, len(numbers)-1
    while start <= end:
        mid = (start+end) // 2
        count = count_range(numbers, start, mid)  # 要的 查找目标数据

        if end == start and count > 1:
            return start

        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1
    return -1


def count_range(numbers, start, end):
    count = 0
    for num in numbers:
        if num >= start and num <= end:
            count += 1
    return count


if __name__ == '__main__':
    numbers = [2, 3, 5, 4, 3, 2, 6, 7]
    print(find_duplications(numbers))
