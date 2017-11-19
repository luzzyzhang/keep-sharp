# -*- coding: utf-8 -*-
"""
    复杂链表的复制
    ~~~~~~~~~~~~~~
    请实现函数clone_complex_link()，复制一个复杂链表。
    在复杂链表中，每个结点除了有一个next指针指向下一个
    结点外，还有一个random 指向链表中的任意结点或者None。
    ~~~~~~~~~~~~~~
    https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def clone_complex_link(head):
    node = head
    while node is not None:
        next_node = node.next

        copy_node = Node(node.val)
        node.next = copy_node
        copy_node.next = next_node

        node = next_node  # or node = copy_node.next

    node = head
    while node is not None:
        if node.random is not None:
            node.next.random = node.random.next
        node = node.next.next

    node = head
    dummy_head = Node(0)
    copy_node = copy_iter = dummy_head
    while node is not None:
        next_node = node.next.next

        copy_node = node.next
        copy_iter.next = copy_node
        copy_iter = copy_node

        node.next = next_node
        node = next_node

    return dummy_head.next


if __name__ == '__main__':
    node1, node2, node3, node4, node5 = Node(1), Node(2), Node(3), Node(4), Node(5)  # noqa
    node1.next, node1.random = node2, node3
    node2.next, node2.random = node3, node5
    node3.next = node4
    node4.next, node4.random = node5, node2

    clone_head = clone_complex_link(node1)
    while clone_head is not None:
        if clone_head.random:
            print(clone_head.val, '-->', clone_head.random.val)
        clone_head = clone_head.next
