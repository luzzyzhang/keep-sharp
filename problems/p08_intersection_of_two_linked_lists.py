# -*- coding: utf-8 -*-
"""
    Intersection of Two Linked Lists
    A:       a1 → a2
                    ↘
                      c1 → c2 → c3
                    ↗
    B:  b1 → b2 → b3
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


# Approach one: time complexity O(m+n), space complexity O(1)
class GetIntersection(object):
    def get_intersection_node(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


# Approach two: time complexity O(m+n), space complexity O(1)
class Solution2(object):
    def length_of_list(self, lst):
        length = 0
        while lst:
            lst = lst.next
            length += 1
        return length

    def jump_steps(self, lst, steps=1):
        for _ in range(steps):
            lst = lst.next
        return lst

    def get_intersection_node(self, headA, headB):
        lengtha = self.length_of_list(headA)
        lengthb = self.length_of_list(headB)

        if lengtha > lengthb:
            headA = self.jump_steps(headA, lengtha - lengthb)
        elif lengtha < lengthb:
            headB = self.jump_steps(headB, lengthb - lengtha)

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


# Approach three use hash table:
# time complexity O(m+n), space complexity O(m) or O(n)
class Solution3(object):
    def get_intersection_node(self, headA, headB):
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next

        while headB:
            if headB in seen:
                return headB
            else:
                headB = headB.next


if __name__ == '__main__':
    same_nodes = ListNode(9, ListNode(11))
    ha = ListNode(1, ListNode(3, ListNode(5, ListNode(7, same_nodes))))
    hb = ListNode(2, ListNode(4, same_nodes))
    # solution = GetIntersection()
    # solution = Solution2()
    solution = Solution3()
    node = solution.get_intersection_node(ha, hb)
    print('The intersection node is {}, value is {}'.format(node, node.val))
