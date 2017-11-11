# -*- coding: utf-8 -*-
"""
    打印二叉树
    ==========
    1. 不分行从上往下打印二叉树
    从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
    ~~~~~~~~~~
    2. 分行从上到下打印二叉树
    从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，
    每一层打印到一行。
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 实际：广度优先遍历二叉树
# 1. 单行
def print_from_top_to_bottom(root):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# 2. 分行，每层一行
def print_muti_lines_from_top_to_bottom(root):
    queue = deque([root])
    current_to_prints = 1   # 当前层还没有打印的节点数目
    next_level_nums = 0     # 下一层的节点数目

    while queue:
        current = queue.popleft()
        print(current.value, end=', ')
        current_to_prints -= 1
        if current.left:
            queue.append(current.left)
            next_level_nums += 1
        if current.right:
            queue.append(current.right)
            next_level_nums += 1

        if current_to_prints == 0:
            print()
            current_to_prints = next_level_nums
            next_level_nums = 0


if __name__ == '__main__':
    root = Node(
        8,
        left=Node(6, left=Node(5), right=Node(7)),
        right=Node(10, left=Node(9), right=Node(11))
    )
    # expect [8, 6, 10, 5, 7, 9, 11]
    print_from_top_to_bottom(root)
    print('不分行打印')
    print(50*'=')
    print('分行打印, 每层一行')
    print_muti_lines_from_top_to_bottom(root)
