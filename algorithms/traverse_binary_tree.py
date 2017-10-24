# -*- coding: utf-8 -*-
"""
    广度遍历
    深度遍历 ：前序遍历，中序遍历，后续遍历
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://en.wikipedia.org/wiki/Tree_traversal#Pre-order
"""

from collections import deque


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bread_first_tranverse(root):
    queue = deque([root])
    while queue:
        current = queue.popleft()  # pop(0) -> O(n); Can use deque optimeize
        yield current.data
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Deepth first Traverse
def bfs_traverse(root):
    if root is None:
        return None
    print(root.data)   # 前序
    if root.left is not None:
        bfs_traverse(root.left)
    # print(root.data)   # 中序
    if root.right is not None:
        bfs_traverse(root.right)
    # print(root.data)   # 后序


def pre_order_iterative(node):
    if node is None:
        return None
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        yield current.data
        # right child is pushed first so that left is processed first
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


def in_order_iterative(node):
    if node is None:
        return None
    stack = []
    while stack or node:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.data
            node = node.right


def post_order_iterative(node):
    stack = []
    last_node_visited = None
    while stack or node:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            # peek_node the value of the top ("front")
            # without removing the element from the collection.
            peek_node = stack[-1]
            # if right child exists and traversing node
            # from left child, then move right
            if peek_node.right and last_node_visited != peek_node.right:
                node = peek_node.right
            else:
                yield peek_node.data
                last_node_visited = stack.pop()


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    node5.left, node5.right = node7, node8
    root = node1
    print('广度遍历')
    print(list(bread_first_tranverse(root)))
    print('深度遍历')
    pre_orders = [1, 2, 4, 5, 7, 8, 3, 6]
    in_orders = [4, 2, 7, 5, 8, 1, 3, 6]
    post_orders = [4, 7, 8, 5, 2, 6, 3, 1]
    assert list(pre_order_iterative(root)) == pre_orders
    assert list(in_order_iterative(root)) == in_orders
    assert list(post_order_iterative(root)) == post_orders
    print(bfs_traverse(root))
