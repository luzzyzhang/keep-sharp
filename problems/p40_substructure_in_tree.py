# -*- coding: utf-8 -*-
"""
    题目：树的子结构
    ~~~~~~~~~~~~~~~
    输入两棵二叉树A和B，判断B是不是A的子结构。
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 树A中找到树B的根节点值一样的节点(递归遍历树)
def has_sub_tree(root1, root2):
    result = False
    if root1 and root2:
        if equal(root1.value, root2.value):
            result = is_sub_tree(root1, root2)
        if not result:
            result = has_sub_tree(root1.left, root2)
        if not result:
            result = has_sub_tree(root1.right, root2)
    return result


# 判断与B树根节点值相同的A的子树是否与B相同(类似与判断两树是否相同)
def is_sub_tree(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False

    if not equal(root1.value, root2.value):
        return False
    is_same_lefts = is_sub_tree(root1.left, root2.left)
    is_same_rights = is_sub_tree(root1.right, root2.right)
    return is_same_lefts and is_same_rights


# 判断浮点数是否相同（注意浮点数比较相等误差问题）
def equal(value1, value2):
    return abs(value1 - value2) < 1e-06
    # return True if abs(value1-value2) < 1e-06 else False


if __name__ == '__main__':
    root1 = Node(
        8,
        left=Node(8, left=Node(9), right=Node(2, left=Node(4), right=Node(7))),
        right=Node(7)
    )
    root2 = Node(8, left=Node(9), right=Node(2))
    assert has_sub_tree(root1, root2)
