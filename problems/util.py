# -*- coding: utf-8 -*-
"""
   Utility functions
"""


class Node:
    def __init__(self, x=None, y=None):
        self.data = x
        self.next = y


def list_to_link(lst):
    if len(lst) == 1:
        return Node(lst[0])
    return Node(lst[0], list_to_link(lst[1:]))
