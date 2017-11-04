# -*- coding: utf-8 -*-
"""
    链表中环的入口结点
    ~~~~~~~~~~~~~~~~~
    一个链表中包含环，如何找出环的入口结点？
    例如，在如下的链表中，环的入口结点是结点3。
    1 -> 2 -> 3 -> 4 -> 5 -> 6
              ^              :
              :              :
              ................
"""


# 入口节点
def entry_node_of_loop(head):
    meet_node = find_meet_node(head)
    if meet_node is None:
        return None

    # 环中节点的数目
    num = 1
    node = meet_node
    while node.next != meet_node:
        node = node.next
        num += 1

    ahead = behind = head
    # ahead 先移动num个节点
    for _ in range(num):
        ahead = ahead.next
    # 同时移动 ahead，behind
    while ahead is not behind:
        ahead = ahead.next
        behind = behind.next

    return ahead


# 如果存在环找到相遇节点
def find_meet_node(head):
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = slow.next

    while fast and slow:
        if fast == slow:
            return fast
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    return None


# 引入额外存储空间记录访问过的节点，如果重复说明是入口节点
def find_entry_node(head):
    if not head or not head.next:
        return None
    seen = set()
    while head:
        if head not in seen:
            seen.add(head)
        else:
            return head
        head = head.next
    return None


if __name__ == '__main__':
    from util import Node
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    assert entry_node_of_loop(node1) == node3
    assert find_entry_node(node1) == node3
