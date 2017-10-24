# -*- coding: utf-8 -*-


def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                swapped = True
    return lst


def bubble_sort2(lst):
    for _ in range(len(lst)):
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]

    return lst


def optimized_bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


if __name__ == '__main__':
    lst = [2, 1, 3, 3, 9, 6]
    print(bubble_sort2(lst))
    print(optimized_bubble_sort(lst))
