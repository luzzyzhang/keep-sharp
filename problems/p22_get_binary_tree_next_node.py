# -*- coding: utf-8 -*-
"""
    二叉树的下一个结点
    ~~~~~~~~~~~~~~~~~
    题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
    树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def get_next(node):
    if node.right is not None:
        right = node.right
        while right.left:
            right = right.left
        next_node = right
    elif node.parent is not None:
        current = node
        parent = node.parent
        while parent and parent.right == current:
            current = parent
            parent = current.parent
        next_node = parent
    return next_node


if __name__ == '__main__':
    node1, node2, node3 = Node(1), Node(2), Node(3)
    node1.left = node2
    node1.right = node3

    node2.parent = node1
    node3.parent = node1

    node = get_next(node2)
    print(node.val)
