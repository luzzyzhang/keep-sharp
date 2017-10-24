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


def construct(pre_orders, mid_orders):
    if (not pre_orders) or (not mid_orders):
        return None

    root_value = pre_orders[0]
    root = Node(root_value)
    if (pre_orders == mid_orders) and len(pre_orders) == 1:
        return root

    try:
        root_index = mid_orders.index(root_value)
    except Exception as e:
        raise e

    left_len = root_index

    if left_len > 0:
        root.left = construct(pre_orders[1:left_len+1],
                              mid_orders[:root_index])

    if left_len < len(pre_orders):
        root.right = construct(pre_orders[left_len+1:],
                               mid_orders[root_index+1:])

    return root


if __name__ == '__main__':
    pre_orders = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_orders = [4, 7, 2, 1, 5, 3, 8, 6]

    root = construct(pre_orders, mid_orders)
    print(root)
