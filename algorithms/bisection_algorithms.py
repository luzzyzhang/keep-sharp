# -*- coding: utf-8 -*-
"""
    Bisection algorithms
    ~~~~~~~~~~~~~~~~~~~~
    https://github.com/python/cpython/blob/3.6/Lib/bisect.py
"""

from bisect import bisect


# Nice example for bisect
# https://docs.python.org/3/library/bisect.html#other-examples
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    Example:
    score = 65 -->  [60, 65, 70, 80, 90] --> i = 1 --> grades[1] = 'D'
    """
    i = bisect(breakpoints, score)
    return grades[i]


def lookup_grades(scores):
    return [grade(score) for score in scores]


# Base binary search
# right 赋值需要注意的问题
# [left, right]: right = n-1 --> while left <= right --> right = middle-1
# [left, right): right = n   --> while left < right  --> right = middle
def binary_search(lst, t):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left+right) // 2
        if lst[mid] < t:
            left = mid + 1
        elif lst[mid] > t:
            right = mid - 1
        else:
            return mid
    return False


# Search lst(sorted and have duplicate elements) return first t's index
# Example: lst = [0, 2, 2, 3], t = 2, return index is 1
def binary_search_first_index(lst, t):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < t:
            left = mid + 1
        else:
            right = mid
    # if left < len(lst) and lst[left] == t:
    if left < len(lst) and lst[left] == t:
        return left
    else:
        return False


# Example: lst = [0, 2, 2, 3], t = 2, return index is 2
def binary_search_last_index(lst, t):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > t:
            right = mid - 1
        else:
            left = mid + 1

    if right < len(lst) and lst[right] == t:
        return right
    else:
        return False


if __name__ == '__main__':
    lst = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8]
    print(lst)
    print(60*'*')
    print(binary_search(lst, 2))
    print(50*'-')
    print(binary_search(lst, 3))
    print(50*'-')
    print(binary_search(lst, 9))
    print(50*'~')
    print(binary_search_first_index(lst, 2))
    print(binary_search_first_index(lst, 3))
    print(binary_search_first_index(lst, 9))
    print(50*'.')
    print(binary_search_last_index(lst, 2))
    print(binary_search_last_index(lst, 3))
    print(binary_search_last_index(lst, 9))
    print(binary_search_first_index([1], 1))
    print(50*'#')
    print('Lookup score to grade')
    scores = [33, 99, 77, 70, 89, 90, 100, 60]
    print(lookup_grades(scores))
