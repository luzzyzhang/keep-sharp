# -*- coding: utf-8 -*-
"""
    题目: 删除链表中的重复节点。在一个排序的链表中，如何删除重复节点?
    例如，1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 to 1 -> 2 -> 5
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""


from util import list_to_link


# 删除重复节点(保留一个删除重复): 1 -> 2 -> 2 -> 3 to 1 -> 2 -> 3
def delete_duplicates(head):
    current = head
    while current is not None and current.next is not None:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


# 删除重复节点(删除全部重复): 1 -> 2 -> 2 -> 3 to 1 -> 3
def delete_duplicate_nodes(head):
    if head is None:
        return None
    pre_node = None
    cur_node = head

    while cur_node is not None:
        next_node = cur_node.next
        need_delete = False
        if next_node is not None and next_node.data == cur_node.data:
            need_delete = True
        if not need_delete:
            pre_node = cur_node
            cur_node = cur_node.next
        else:
            value = cur_node.data
            delete_node = cur_node
            while delete_node is not None and delete_node.data == value:
                next_node = delete_node.next
                del delete_node
                delete_node = None
                delete_node = next_node
            if pre_node is None:
                head = next_node
            else:
                pre_node.next = next_node
            cur_node = next_node


if __name__ == '__main__':
    link = list_to_link([1, 2, 3, 3, 4, 4, 5])
    # delete_duplicate_nodes(link)
    delete_duplicates(link)
    while link:
        print(link.data)
        link = link.next
