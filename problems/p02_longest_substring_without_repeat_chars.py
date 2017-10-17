# -*- coding: utf-8 -*-


def len_of_longest_substring_brute_force(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if len(s[i:j]) == len(set(s[i:j])):  # or len(set(s[i:j]) == j-i
                max_len = max(max_len, j-i)
    return max_len


def len_of_longest_substring_slide_window(s):
    max_len = 0
    left = 0
    visited = {}
    for right, char in enumerate(s):
        if char in visited and visited[char] >= left:
            left = visited[char] + 1
        max_len = max(max_len, right-left+1)
        visited[char] = right
    return max_len


if __name__ == '__main__':
    test, expect = 'abcabcbb', 3  # 'abc'
    assert len_of_longest_substring_brute_force(test) == expect
    assert len_of_longest_substring_slide_window(test) == expect
