# -*- coding: utf-8 -*-
"""
   Utility functions
"""

from random import randrange


class Node:
    def __init__(self, x=None, y=None):
        self.data = x
        self.next = y


def list_to_link(lst):
    if len(lst) == 1:
        return Node(lst[0])
    return Node(lst[0], list_to_link(lst[1:]))


def partition(lst, left, right):
    pivot = randrange(left, right)
    pivot_value = lst[pivot]
    index = left

    lst[pivot], lst[right] = lst[right], lst[pivot]

    for i in range(left, right):
        if lst[i] <= pivot_value:
            lst[i], lst[index] = lst[index], lst[i]
            index += 1
    lst[right], lst[index] = lst[index], lst[right]
    return index
