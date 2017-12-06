# -*- coding: utf-8 -*-
"""
"""


def two_sum_in_sorted_array(data, target):
    left, right = 0, len(data)-1

    while right > left:
        current_sum = data[right] + data[left]
        if current_sum == target:
            return {data[right], data[left]}
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return -1


if __name__ == '__main__':
    # TODO test
    pass
