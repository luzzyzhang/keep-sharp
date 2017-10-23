# -*- coding: utf-8 -*-
"""
    从尾到头打印链表
    ~~~~~~~~~~~~~~~
    题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_link_list_reverse_iter(head):
    stack = []
    while head is not None:
        stack.append(head)
        head = head.next

    while stack:
        node = stack.pop()
        print(node.val)


def print_link_list_reverse_recursive(head):
    if head is not None:
        print_link_list_reverse_recursive(head.next)
        print(head.val)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print_link_list_reverse_iter(node1)
    print_link_list_reverse_recursive(node1)
