# -*- coding: utf-8 -*-
"""
   插入排序
   ~~~~~~~
   https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
"""


def insert_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst


def insert_sort2(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = tmp
    return lst


if __name__ == '__main__':
    lst = [9, 3, 4, 5, 7, 6, 2, 1, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert insert_sort(lst) == expected
    assert insert_sort2(lst) == expected
