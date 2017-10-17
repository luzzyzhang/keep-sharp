# -*- coding: utf-8 -*-


def len_of_longest_substring(s):

    def all_unique(string):
        return True if len(string) == len(set(string)) else False

    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if all_unique(s[i:j]):
                max_len = max(max_len, j-i)
    return max_len


if __name__ == '__main__':
    test1, expect1 = 'abcabcbb', 3  # 'abc'
    test2, expect2 = 'bbbbb', 1  # 'b'
    test3, expect3 = 'pwwkew', 3  # 'wke'
    assert len_of_longest_substring(test1) == expect1
    assert len_of_longest_substring(test2) == expect2
    assert len_of_longest_substring(test3) == expect3
    long_string = ("lursenhsaqzomihhopmfffywxjxnbsgonzitmq"
                   "loilduvkblansfvqdubahcupshobccrqrzd")
    print(len_of_longest_substring(long_string))
