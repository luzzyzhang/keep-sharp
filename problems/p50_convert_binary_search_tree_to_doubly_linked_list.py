# -*- coding: utf-8 -*-
"""
    二叉搜索树与双向链表
    ~~~~~~~~~~~~~~~~~~~~
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class Node:
    """二叉搜索树结点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert_bst_to_doubly_linked_list(root):
    last_list_node = LinkNode(None)
    convert_node(root, last_list_node)
    # 返回双向链表的头结点
    head = last_list_node
    while head is not None and head.left is not None:
        head = head.left
    return head


# 根据二叉搜索树特点和题目要求之排序双向链表，采用中序遍历二叉搜索树
def convert_node(bst_node, last_list_node):
    if bst_node is None:
        return None
    current = bst_node

    if current.left is not None:
        convert_node(current.left, last_list_node)

    current.left = last_list_node
    if last_list_node is not None:
        last_list_node.right = current
    last_list_node = current

    if current.right is not None:
        convert_node(current.right, last_list_node)


if __name__ == '__main__':
    node4, node6, node8, node10 = Node(4), Node(6), Node(8), Node(10)
    node12, node14, node16 = Node(12), Node(14), Node(16)
    node10.left, node10.right = node6, node14
    node6.left, node6.right = node4, node8
    node14.left, node14.right = node12, node16

    root = node10
    head = convert_bst_to_doubly_linked_list(root)
    # while head:
    #     print(head.val)
    #     head = head.right
