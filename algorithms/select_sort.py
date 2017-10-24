# -*- coding: utf-8 -*-
"""
    选择排序
    ~~~~~~~
    https://en.wikipedia.org/wiki/Selection_sort
"""


def select_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == '__main__':
    lst = [8, 9, 7, 5, 4, 6, 3, 2, 1]
    assert select_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
