# -*- coding: utf-8 -*-
"""
    题目: 调整数组顺序使奇数位于偶数前面
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""


def odd_even_reorder(lst):
    return sorted(lst, key=lambda x: not x & 0x1)


def odd_even_reorder1(lst):
    odd = [x for x in lst if x & 0x1]
    even = [y for y in lst if not y & 0x1]
    return odd + even


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    assert odd_even_reorder(lst) == [1, 3, 5, 7, 2, 4, 6, 8]
    assert odd_even_reorder1(lst) == [1, 3, 5, 7, 2, 4, 6, 8]
