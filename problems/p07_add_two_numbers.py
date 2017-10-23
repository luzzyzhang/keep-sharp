# -*- coding: utf-8 -*-
"""
    https://leetcode.com/problems/add-two-numbers/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
"""

from util import Node, list_to_link


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: Node
        :type l2: Node
        :rtype: Node
        """
        carry = 0
        head = Node(0)
        curr = head
        head1, head2 = l1, l2
        while head1 or head2:
            x = head1.data if head1 else 0
            y = head2.data if head2 else 0

            sum = carry + x + y
            carry = sum // 10
            curr.next = Node(sum % 10)

            curr = curr.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        if carry > 0:
            curr.next = Node(carry)
        return head.next


if __name__ == '__main__':
    head1 = list_to_link([2, 4, 3])
    head2 = list_to_link([5, 6, 4])
    solution = Solution()
    r = solution.add_two_numbers(head1, head2)
    while r:
        print(r.data)
        r = r.next
