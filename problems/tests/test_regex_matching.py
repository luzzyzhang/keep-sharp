
import pytest

from problems.p35_regex_match import (ismatch, ismatch_top_down_dp, ismatch_bottom_up_dp)  # noqa


test_params = [
    ("", "", True),
    ("", ".*", True),
    ("", "c*", True),
    ("a", "a.", False),
    ("a", "ab*", True),
    ("a", "", False),
    ("aa", "a", False),
    ("aa", "aa", True),
    ("aaa", "aa", False),
    ("aa", "a*", True),
    ("aa", ".*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("a", "ab*", True),
    ("a", "ab*a", False),
    ("aa", "aa", True),
    ("aa", "a*", True),
    ("aa", ".*", True),
    ("aa", ".", False),
    ("ab", ".*", True),
    ("ab", ".*", True),
    ("aaa", "aa*", True),
    ("aaa", "aa.a", False),
    ("aaa", "a.a", True),
    ("aaa", ".a", False),
    ("aaa", "a*a", True),
    ("aaa", "ab*a", False),
    ("aaa", "ab*ac*a", True),
    ("aaa", "ab*a*c*a", True),
    ("aaa", ".*", True),
    ("aab", "c*a*b", True),
    ("aaca", "ab*a*c*a", True),
    ("aaba", "ab*a*c*a", False),
    ("bbbba", ".*a*a", True),
    ("bcbbabab", ".*a*a", False),
]


@pytest.mark.parametrize('string, pattern, expected', test_params)
def test_regex_match(string, pattern, expected):
    assert ismatch(string, pattern) is expected
    assert ismatch_top_down_dp(string, pattern) is expected
    assert ismatch_bottom_up_dp(string, pattern) is expected
