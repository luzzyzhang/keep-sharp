# -*- coding: utf-8 -*-
"""
    Swap nodes in pairs
    ~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""


class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


# pre-->a-->b-->b.next to pre-->b-->a-->b.next
# Iterative approach
def swap_pairs(head):
    dummy = pre = Node()
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return dummy.next


# Recursive approach, extra O(n) space complexity due to recursive use stack
# head --> node --> [nodes_all_swaped] to node --> head --> [nodes_all_swapped]
def swap_node_pairs_recursive(head):
    if head is None or head.next is None:
        return head
    node = head.next
    head.next = swap_node_pairs_recursive(head.next.next)
    node.next = head
    return node


if __name__ == '__main__':
    node1, node2, node3, node4, = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # r = swap_pairs(node1)
    r = swap_node_pairs_recursive(node1)
    while r:
        print(r.val)
        r = r.next
