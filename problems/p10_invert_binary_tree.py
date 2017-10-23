# -*- coding: utf-8 -*-

"""
    Invert binary tree
    ~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/invert-binary-tree/description/
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root

    def iterative_invert_tree(self, root):
        from collections import deque
        queue = deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return root
