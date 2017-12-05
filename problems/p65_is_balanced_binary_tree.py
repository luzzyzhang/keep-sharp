# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/balanced-binary-tree/discuss/
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Top-down approach
class Solution:
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def is_banlanced(self, root):
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return (abs(left-right) <= 1 and
                self.is_banlanced(root.left) and self.is_banlanced(root.right))


# Buttom-up, post-order deep first search
class Solution2:
    def dfs_height(self, root):
        if root is None:
            return 0
        left_height = self.dfs_height(root.left)
        if left_height == -1:
            return -1
        right_height = self.dfs_height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
                return -1
        return max(left_height, right_height) + 1

    def is_balanced(self, root):
        return self.dfs_height(root) != -1


if __name__ == '__main__':
    # TODO test
    pass
