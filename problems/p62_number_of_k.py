# -*- coding: utf-8 -*-
"""
"""


def get_number_k(numbers, k):
    rv = 0
    first_k = get_first_k(numbers, k)
    last_k = get_last_k(numbers, k)
    if first_k > -1 and last_k > -1:
        rv = last_k - first_k + 1
    return rv


def get_last_k(numbers, k):
    left, right = 0, len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > k:
            right = mid - 1
        else:
            left = mid

    if right < len(numbers) and numbers[right] == k:
        return right
    else:
        return -1


def get_first_k(numbers, k):
    left, right = 0, len(numbers)-1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < k:
            left = mid + 1
        else:
            right = mid
    if left < len(numbers) and numbers[left] == k:
        return left
    else:
        return -1


if __name__ == '__main__':
    numbers = [1, 2, 3, 3, 3, 3, 4, 5]
    numbers2 = [3, 3, 3, 3, 4, 5]
    assert get_number_k(numbers, 3) == 4
    assert get_number_k(numbers2, 3) == 4
