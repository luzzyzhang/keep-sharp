# -*- coding: utf-8 -*-
"""
    Quicksort
    ~~~~
    https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F#Python
"""


from random import randrange


def qsort0(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [x for x in lst[1:] if x < pivot]
    greater = [y for y in lst[1:] if y > pivot]
    return qsort0(less) + [pivot] + qsort0(greater)


def qsort1(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less, greater = [], []

    for i in lst[1:]:
        if i < pivot:
            less.append(i)
        elif i >= pivot:
            greater.append(i)
    return qsort1(less) + [pivot] + qsort1(greater)


# 原地分区版：空间复杂度 O(logn)
def partition(lst, left, right):
    pivot = randrange(left, right)
    pivot_value = lst[pivot]
    index = left

    lst[pivot], lst[right] = lst[right], lst[pivot]

    for i in range(left, right):
        if lst[i] <= pivot_value:
            lst[i], lst[index] = lst[index], lst[i]
            index += 1
    lst[right], lst[index] = lst[index], lst[right]
    return index


def qsort(lst, left, right):
    if right > left:
        pivot = partition(lst, left, right)
        qsort(lst, left, pivot-1)
        qsort(lst, pivot+1, right)


if __name__ == '__main__':
    lst = [5, 6, 78, 9, 0, -1, 2, 3, -65, 12]
    qsort(lst, 0, len(lst)-1)
    print(lst)
