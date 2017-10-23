# -*- coding: utf-8 -*-
"""
    Largest number
    ~~~~~~~~~~~~~
    For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
    https://leetcode.com/problems/largest-number/
"""


# def largest_number(nums):
#     nums = map(str, nums)
#     nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
#     return ''.join(nums).lstrip('0') or '0'
#
#
# def largest_number2(nums):
#     import itertools
#     return ''.join(sorted(itertools.imap(str, nums),
#                           cmp=lambda x, y: cmp(y+x, x+y))).lstrip('0') or '0'


# Python3 remove cmp to key
# https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter
def largest_number(nums):
        from functools import cmp_to_key

        def compare(x, y):
            print(x, y)
            return 1 if y + x > x + y else -1
        return ''.join(sorted([str(n) for n in nums],
                       key=cmp_to_key(compare))).lstrip('0') or '0'


def test():
    lst = [3, 30, 34, 5, 9]
    r = largest_number(lst)
    print(r)
    assert r == '9534330'
    print('test pass')


if __name__ == '__main__':
    print(test())
