# -*- coding: utf-8 -*-
"""
    Merge sort, 归并排序
    ~~~~~
    Time complexity: O(nlogn); Space complexity: O(n)
    ~~~~~
    https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    ~~~~~
    https://www.youtube.com/watch?v=EeQ8pwjQxTM
"""


from collections import deque


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            # deque popleft() is O(1) complexity
            smaller = left.popleft() if left[0] < right[0] else right.popleft()
            merged.append(smaller)
        # merged.extend(right if right else left)
        # or merged.extend(right+left)
        # or merged.extend(right or left)
        merged += left or right
        return list(merged)

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)


if __name__ == '__main__':
    lst = [6, 5, 3, 1, 8, 7, 2, 4]
    r = merge_sort(lst)
    print(r)
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]
