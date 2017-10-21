# -*- coding: utf-8 -*-
"""
   合并两个有序链表
"""
from util import Node


# Recursion version
def merge(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    merged_head = Node()

    if head1.data < head2.data:
        merged_head = head1
        merged_head.next = merge(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge(head1, head2.next)
    return merged_head


# Iteration version
def iterate_merge(head1, head2):
    head = current = Node()
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    current.next = head1 or head2
    return head.next


if __name__ == '__main__':
    from util import list_to_link
    lst1 = [1, 3, 5, 7, 9]
    lst2 = [2, 4, 6, 8, 10]
    link1 = list_to_link(lst1)
    link2 = list_to_link(lst2)
    # r = merge(link1, link2)
    r = iterate_merge(link1, link2)

    def result(link):
        while link:
            yield link.data
            link = link.next
    print([i for i in result(r)])
