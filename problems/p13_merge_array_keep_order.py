# -*- coding: utf-8 -*-

from collections import deque


def merge_two_list_keep_order(l1, l2):
    """
    Merge l1 and l2, keep the order
    """
    result = []
    while l1 and l2:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))  # lst.pop(0) time complexity is O(n)
        else:
            result.append(l2.pop(0))
    result.extend(l1 + l2)
    return result


def merge_two_list_keep_order_with_deque(lst1, lst2):
    """Use deque for performance; deque popleft() is O(1) complexity;
    Better than list pop(0) O(n) complexity.
    """
    result, q1, q2 = deque(), deque(lst1), deque(lst2)
    while q1 and q2:
        smaller = q1.popleft() if q1[0] <= q2[0] else q2.popleft()
        result.append(smaller)
    result.extend(q1 + q2)
    return list(result)


if __name__ == '__main__':
    l1 = [1, 3, 2, 4, 5, 7]
    l2 = [2, 4, 1, 3, 0, 7]
    r = merge_two_list_keep_order(l1, l2)
    print(r)
    assert r == [1, 2, 3, 2, 4, 1, 3, 0, 4, 5, 7, 7]

    l3 = [4, 15, 16, 50]
    l4 = [8, 23, 42, 108]
    expect = [4, 8, 15, 16, 23, 42, 50, 108]
    assert merge_two_list_keep_order(l3, l4) == expect
