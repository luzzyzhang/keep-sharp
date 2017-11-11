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
    3. 之字形打印二叉树
    ~~~~~~~~~~~~~~~~~~
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺
    序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，
    其他行以此类推。
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


# 3. 之字行打印二叉树, 使用两个栈
def print_tree_in_zigzag(root):
    current_stack = []
    next_stack = []
    left_to_right = True
    current_stack.append(root)

    while current_stack:
        current_node = current_stack.pop()
        if current_node:
            print(current_node.value, end=',')
            if left_to_right:
                next_stack.append(current_node.left)
                next_stack.append(current_node.right)
            else:
                next_stack.append(current_node.right)
                next_stack.append(current_node.left)
        if len(current_stack) == 0:
            print()
            left_to_right = not left_to_right
            current_stack, next_stack = next_stack, current_stack


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
    print(50*'=')
    print('之字形打印二叉树')
    node1, node2, node3, node4, node5, node6 = (Node(i) for i in range(1, 7))
    node7, node8, node9, node10, node11, node12 = (Node(i) for i in range(7, 13))  # NOQA
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11
    node6.left = node12
    print_tree_in_zigzag(node1)
