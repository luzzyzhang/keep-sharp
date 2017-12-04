# -*- coding: utf-8 -*-
"""
    二叉搜索树的第k个结点
    ~~~~~~~~~~~~~~~~~~~~~
    给定一棵二叉搜索树，请找出其中的第k大的结点。
    https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/
"""

# 中序遍历二叉搜索树的到递增排序的序列


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node({})'.format(self.val)


def kth_node_in_bst(root, k):
    target = None
    if root.left is not None:
        target = kth_node_in_bst(root.left, k)

    if target is None:
        if k == 1:
            target = root
        k -= 1

    if target is None and root.right is not None:
        target = kth_node_in_bst(root.right, k)
    return target


def kth_node_in_bst2(root, k):
    count = []
    in_order_tranvere(root, count)
    return count[k-1]

def in_order_tranvere(node, count):
    if not node:
        return
    in_order_tranvere(node.left, count)
    count.append(node.val)
    in_order_tranvere(node.right, count)


if __name__ == '__main__':
    node2, node3, node4, node5 = Node(2), Node(3), Node(4), Node(5)
    node6, node7, node8 = Node(6), Node(7), Node(8)
    node5.left, node5.right = node3, node7
    node3.left, node3.right = node2, node4
    node7.left, node7.right = node6, node8
    expect = 6
    root = node5
    node = kth_node_in_bst2(node5, 5)

    assert node == expect, 'Invalid node {}'.format(node)
