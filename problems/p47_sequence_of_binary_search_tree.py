# -*- coding: utf-8 -*-
"""
    二叉搜索树的后序遍历序列
    ~~~~~~~~~~~~~~~~~~~~~~~
    题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
    ~~~~~~~~~~~~~~~~~~~~~~
    参考维基百科：二叉搜索树
"""


def is_bst_post_order_sequence(sequences):
    if not sequences:
        return False
    if len(sequences) == 3:
        root = sequences[-1]
        return sequences[0] < root and sequences[1] > root
    elif len(sequences) == 2:
        return sequences[0] < sequences[1]
    elif len(sequences) == 1:
        return True
    elif sequences in (sorted(sequences), sorted(sequences, reverse=True)):
        return True

    lefts = [i for i in sequences[:-1] if i < sequences[-1]]
    rights = [i for i in sequences[:-1] if i > sequences[-1]]
    return is_bst_post_order_sequence(lefts) and is_bst_post_order_sequence(rights)  # noqa


if __name__ == '__main__':
    lst = [5, 7, 6, 9, 11, 10, 8]
    assert is_bst_post_order_sequence(lst) is True
