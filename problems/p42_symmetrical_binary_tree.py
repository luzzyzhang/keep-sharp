# -*- coding: utf-8 -*-
"""
    对称的二叉树
    ~~~~~~~~~~~
    请实现一个函数，用来判断一棵二叉树是不是对称的。
    如果一棵二叉树和它的镜像一样，那么它是对称的。
    ~~~~~~~~~~
    真是无聊的问题!
"""


def is_symmetric(root):
    return compare_tree(root, root)


def compare_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    return (compare_tree(root1.left, root2.right) and
            compare_tree(root1.right,  root2.left))
