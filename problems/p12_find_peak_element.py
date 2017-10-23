# -*- coding: utf-8 -*-
"""
    Find peak element
    ~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/find-peak-element/
"""


# Solution1
def find_peak(nums):
    nums = [float('-inf')] + nums + [float('-inf')]
    for i in range(1, len(nums)-1):
        # if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i-1
    return None


if __name__ == '__main__':
    assert find_peak([1, 2, 3, 1]) == 2
    assert find_peak([1]) == 0
    assert find_peak([]) is None
