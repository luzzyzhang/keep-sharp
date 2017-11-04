# -*- coding: utf-8 -*-
"""
    题目：树的子结构
    ~~~~~~~~~~~~~~~
    输入两棵二叉树A和B，判断B是不是A的子结构。
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
