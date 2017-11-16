# -*- coding: utf-8 -*-
"""
    二叉树中和为某一值的路径
    ~~~~~~~~~~~~~~~~~~~~~~~~
    输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
    有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
    ~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/path-sum-ii/description/
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 1. DFS: 前序遍历二叉树(因为从root->leaf), 递归法，先分析只有一个根节点
def path_sum(root, target):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]] if root.val == target else []
    lefts = path_sum(root.left, target-root.val)
    rights = path_sum(root.right, target-root.val)
    return [[root.val] + path for path in lefts+rights]


# 2. Depth First Search use Stack -- 递归实质为栈调用(入栈，出栈)
def path_sum_dfs_iterative(root, target):
    if not root:
        return []
    stack = [(root, [root.val])]
    while stack:
        current, path = stack.pop()
        if (not current.left and not current.right and sum(path) == target):
            yield path
        if current.right:
            stack.append((current.right, path+[current.right.val]))
        if current.left:
            stack.append((current.left, path+[current.left.val]))


# 3. Broad First Search use Queue
def path_sum_bfs(root, target):
    from collections import deque
    if not root:
        return []
    queue = deque([(root, [root.val])])
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right and sum(path) == target:
            yield path
        if node.left:
            queue.append((node.left, path+[node.left.val]))
        if node.right:
            queue.append((node.right, path+[node.right.val]))


if __name__ == '__main__':
    node10, node5, node12, node4, node7 = Node(10), Node(5), Node(12), Node(4), Node(7)  # noqa
    node10.left, node10.right = node5, node12
    node5.left, node5.right = node4, node7
    root = node10
    expected = [[10, 5, 7], [10, 12]]
    assert path_sum(root, 22) == expected
    assert list(path_sum_dfs_iterative(root, 22)) == expected
    assert list(path_sum_bfs(root, 22)) in (expected, expected[::-1])
