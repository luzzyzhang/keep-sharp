
import pytest

from problems.p02_longest_substring_without_repeat_chars import (
        len_of_longest_substring_brute_force,
        len_of_longest_substring_slide_window,
        len_of_longest_substring_dynamic,
)


long_string = ("lursenhsaqzomihhopmfffywxjxnbsgonzitmq"
               "loilduvkblansfvqdubahcupshobccrqrzd")

test_params = [
    ('', 0),
    ('a', 1),
    ('abcabcbb', 3),
    ('abcacfrar', 4),
    ('acfrarabc', 4),
    ('arabcacfr', 4),
    ('aaabbbccc', 2),
    ('abcdcba', 4),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('abcdef', 6),
    (long_string, 11)
]


@pytest.mark.parametrize('string, expected', test_params)
def test_longest_substring_no_repeat_chars(string, expected):
    assert len_of_longest_substring_brute_force(string) == expected
    assert len_of_longest_substring_slide_window(string) == expected
    assert len_of_longest_substring_dynamic(string) == expected
