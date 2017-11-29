# -*- coding: utf-8 -*-
"""
"""


def permutations(string, begin=0):
    if begin == len(string)-1:
        print(string)
    else:
        for char in string[begin:]:
            string[begin], char = char, string[begin]
            permutations(string, begin+1)
            string[begin], char = char, string[begin]


if __name__ == '__main__':
    string = 'abc'
    permutations(list(string))
