# -*- coding: utf-8 -*-
"""
    连续子数组的最大和
    ~~~~~~~~~~~~~~~~~
    输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
    数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
"""


def largest_sum_of_subarray(numbers):
    if not numbers:
        return 0
    current_sum = 0
    largest_sum = float('-inf')

    for i, num in enumerate(numbers):
        if current_sum <= 0:
            current_sum = num
        else:
            current_sum += num
        if current_sum > largest_sum:
            largest_sum = current_sum
    return largest_sum


if __name__ == '__main__':
    numbers = [1, -2, 3, 10, -4, 7, 2, -5]
    numbers2 = [-2, -8, -1, -5, -9]
    assert largest_sum_of_subarray(numbers) == 18
    assert largest_sum_of_subarray(numbers2) == -1
