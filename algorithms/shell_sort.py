# -*- coding: utf-8 -*-
"""
    Shellsort
    ~~~~~~~~~
    https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F#Python
"""


def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j-gap] > tmp:
                lst[j] = lst[j-gap]
                j -= gap
            lst[j] = tmp
        gap = gap // 2
    return lst


if __name__ == '__main__':
    lst = [9, 3, 2, 1, 8, 6, 4, 5, 7]
    assert shell_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
