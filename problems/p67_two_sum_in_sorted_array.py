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


def continue_sequence_of_sum(target):
    if target < 3:
        return
    small, big = 1, 2
    middle = (1+target) // 2
    current_sum = small + big

    while small < big:
        if current_sum == target:
            yield (small, big)
        while current_sum > target and small < middle:
            current_sum -= small
            small += 1

            if current_sum == target:
                yield (small, big)
        big += 1
        current_sum += big


if __name__ == '__main__':
    # TODO test
    pass
