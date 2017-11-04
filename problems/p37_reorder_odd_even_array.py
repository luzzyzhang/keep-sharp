# -*- coding: utf-8 -*-
"""
    题目: 调整数组顺序使奇数位于偶数前面
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""


def odd_even_reorder(lst):
    # return sorted(lst, key=lambda x: not x & 0x1)
    lst.sort(key=lambda x: not x & 0x1)   # stable sort *IN PLACE*
    return lst


def odd_even_reorder1(lst):
    odd = [x for x in lst if x & 0x1]
    even = [y for y in lst if not y & 0x1]
    return odd + even


# 双指针法
def reorder_odd_even(lst):
    head, end = 0, len(lst)-1

    while head < end:
        while lst[head] & 0x1 == 1:
            head += 1
        while lst[end] & 0x1 == 0:
            end -= 1
        if head < end:
            head, end = end, head
    return lst


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expect = [1, 3, 5, 7, 2, 4, 6, 8]
    assert odd_even_reorder(lst) == expect
    assert odd_even_reorder1(lst) == expect
    assert reorder_odd_even(lst) == expect
