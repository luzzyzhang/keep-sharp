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


def len_of_longest_substring_dynamic(s):
    cur_len = 0
    max_len = 0
    position = [-1 for _ in range(26)]

    for i in range(len(s)):
        prev_index = position[ord(s[i]) - ord('a')]
        if prev_index < 0 or i - prev_index > cur_len:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev_index
        position[ord(s[i]) - ord('a')] = i
    if cur_len > max_len:
        max_len = cur_len
    return max_len


if __name__ == '__main__':
    test, expect = 'abcabcbb', 3  # 'abc'
    assert len_of_longest_substring_brute_force(test) == expect
    assert len_of_longest_substring_slide_window(test) == expect
    assert len_of_longest_substring_dynamic(test) == expect
