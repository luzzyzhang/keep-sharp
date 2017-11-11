# -*- coding: utf-8 -*-
"""
    不分行从上往下打印二叉树
    ~~~~~~~~~~~~~~~~~~~~~~~
    从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 实际：广度优先遍历二叉树
def print_from_top_to_bottom(root):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        yield current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == '__main__':
    root = Node(
        8,
        left=Node(6, left=Node(5), right=Node(7)),
        right=Node(10, left=Node(9), right=Node(11))
    )
    assert list(print_from_top_to_bottom(root)) == [8, 6, 10, 5, 7, 9, 11]
