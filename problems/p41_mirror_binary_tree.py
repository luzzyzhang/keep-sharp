# -*- coding: utf-8 -*-
"""
    二叉树的镜像
    ~~~~~~~~~~~
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
    实际上反转二叉树
"""


def mirror_binary_tree(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return None

    node.left, node.right = node.right, node.left

    if node.lfet:
        mirror_binary_tree(node.left)
    if node.right:
        mirror_binary_tree(node.right)
