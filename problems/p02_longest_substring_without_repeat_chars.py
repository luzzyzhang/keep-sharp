# -*- coding: utf-8 -*-


def len_of_longest_substring_brute_force(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if len(s[i:j]) == len(set(s[i:j])):  # or len(set(s[i:j]) == j-i
                max_len = max(max_len, j-i)
    return max_len


if __name__ == '__main__':
    test, expect = 'abcabcbb', 3  # 'abc'
    assert len_of_longest_substring_brute_force(test) == expect
