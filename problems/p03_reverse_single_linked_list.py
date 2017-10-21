# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Iteractive version, time complexity O(n), space complexity O(1)
#        1-->2-->3-->4-->5-->None
# None<--1<--2<--3<--4<--5
def reverse_linked_list_iteract(head):
    prev = None
    while head is not None:
        head.next, prev, head = prev, head, head.next
    return prev


# Recursive version
# time complexity O(n), space complexity O(n), stack due to recursion
def reverse_linked_list_recusive(head):
    if head is None or head.next is None:
        return head
    node = reverse_linked_list_iteract(head.next)
    head.next.next = head
    head.next = None
    return node


if __name__ == '__main__':
    my_link = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    # link = reverse_linked_list_iteract(my_link)
    link = reverse_linked_list_recusive(my_link)
    while link:
        print(link.data)
        link = link.next
