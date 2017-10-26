# -*- coding: utf-8 -*-
"""
    删除链表的节点
    ~~~~~~~~~~~~~
    题目1: 在 O(1) 时间内删除链表节点。
           给定单向链表的头指针和一个节点指针，定义函数在 O(1) 时间内删除该节点。
    题目2: 删除链表中的重复节点。在一个排序的链表中，如何删除重复节点?
           例如，1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 to 1 -> 2 -> 5
"""


from util import list_to_link


def delete_node(head, to_del_node):
    if head is None or to_del_node is None:
        return None

    if to_del_node.next is not None:    # 要删除节点非尾节点
        tmp = to_del_node.next
        to_del_node.data = tmp.data
        to_del_node.next = tmp.next
        del tmp
        tmp = None
    elif head == to_del_node:           # 链表只有一个节点，删除头尾节点
        del to_del_node
        del head
        head = None
        to_del_node = None
    else:                               # 链表中多个节点，删除尾节点
        node = head
        while node.next != to_del_node:
            node = node.next
        del to_del_node
        node.next = None


if __name__ == '__main__':
    link = list_to_link([1, 2, 3, 4, 5])
    delete_node(link, link.next.next.next.next)
    while link:
        print(link.data)
        link = link.next
