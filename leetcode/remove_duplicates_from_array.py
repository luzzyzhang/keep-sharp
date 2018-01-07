"""
    Remove Duplicates from Sorted Array
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""


# Time Limit Exceeded
def remove_duplicates1(nums):
    for num in nums:
        while nums.count(num) >= 2:
            nums.remove(num)
    return len(nums)


# Two pointers, time complexity O(n), space complexity O(1)
def remove_duplicates2(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3]
    expect = 3
    assert remove_duplicates1(nums) == expect
    assert remove_duplicates2(nums) == expect
