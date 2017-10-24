# -*- coding: utf-8 -*-
"""
    重建二叉树
    ~~~~~~~~~~
    题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
    假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列
    {1, 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，
    则重建出二叉树并输出它的头结点。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self, depth=0):
        ret = ""
        # Print right branch
        if self.right is not None:
            ret += self.right.__str__(depth + 1)
        # Print own value
        ret += "\n" + ("    "*depth) + str(self.val)
        # Print left branch
        if self.left is not None:
            ret += self.left.__str__(depth + 1)
        return ret


def construct(preorders, inorders):
    if (not preorders) or (not inorders):
        return None

    root_value = preorders[0]
    root = Node(root_value)
    if (preorders == inorders) and len(preorders) == 1:
        return root

    try:
        root_index = inorders.index(root_value)
    except Exception as e:
        raise e

    left_len = root_index

    if left_len > 0:
        root.left = construct(preorders[1:left_len+1],
                              inorders[:root_index])

    if left_len < len(preorders):
        root.right = construct(preorders[left_len+1:],
                               inorders[root_index+1:])

    return root


if __name__ == '__main__':
    preorders = [1, 2, 4, 7, 3, 5, 6, 8]
    inorders = [4, 7, 2, 1, 5, 3, 8, 6]

    root = construct(preorders, inorders)
    print(root)
