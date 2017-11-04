# -*- coding: utf-8 -*-
"""
    题目：链表中倒数第k个结点
    ~~~~~~~~~~~~~~~~~~~~~~~~
    输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
    本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
    从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
    值为4的结点。
"""


def find_kth_tail_node(head, k):
    if not head or k == 0:
        return None
    ahead = behind = head
    for _ in range(k-1):
        if ahead.next is not None:
            ahead = ahead.next
        else:
            return None
    while ahead.next is not None:
        ahead = ahead.next
        behind = behind.next
    return behind


if __name__ == '__main__':
    from util import list_to_link
    link = list_to_link([1, 2, 3, 4, 5, 6])
    assert find_kth_tail_node(link, 1).data == 6
    assert find_kth_tail_node(link, 6).data == 1
    assert find_kth_tail_node(link, 4).data == 3
    assert find_kth_tail_node(link, 100) is None

