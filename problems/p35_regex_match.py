# -*- coding: utf-8 -*-
"""
    正则表达式匹配
    ~~~~~~~~~~~~~
    题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'
    表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题
    中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
    和"ab*ac*a"匹配，但与"aa.a"及"ab*a"均不匹配。
    ~~~~~~~~~~~~~~
    https://leetcode.com/problems/regular-expression-matching/description/
"""


# Recursion Approach
# Without a start (*), straightforward:
def match(string, pattern):
    if not pattern:
        return not string
    first_match = bool(string) and pattern[0] in {string[0], '.'}
    return first_match and match(string[1:], pattern[1:])


def ismatch(string, pattern):
    if not pattern:
        return not string
    first_match = bool(string) and pattern[0] in {string[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return (ismatch(string, pattern[2:]) or
                first_match and ismatch(string[1:], pattern))
    else:
        return first_match and ismatch(string[1:], pattern[1:])


# Dynamic Programming Approach
# Top-Down Variation
def ismatch_top_down_dp(string, pattern):
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = (i == len(string))
            else:
                first_match = i < len(string) and pattern[j] in {string[i], '.'}  # noqa
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0, 0)


# Bottom-Up
def ismatch_bottom_up_dp(string, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]

    dp[-1][-1] = True
    for i in range(len(string), -1, -1):
        for j in range(len(pattern)-1, -1, -1):
            first_match = i < len(string) and pattern[j] in {string[i], '.'}
            if j+1 < len(pattern) and pattern[j+1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]
    return dp[0][0]


if __name__ == '__main__':
    assert ismatch('aaa', 'ab*ac*a')
    assert not match('aaa', 'aa.a')
    assert not ismatch_top_down_dp('aaa', 'ab*a')
    assert not ismatch_bottom_up_dp('aaa', 'ab*a')
