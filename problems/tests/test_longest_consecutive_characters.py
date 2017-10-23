
import pytest

from problems.p11_longest_consecutive_charaters import longest_cons_char


test_params = [('AABCDDBBBEA', {'B': 3}),
               ('AAA', {'A': 3}),
               ('', {None: 0}),
               ('ABC', {'C': 1})]


@pytest.mark.parametrize('s, r', test_params)
def test_longest_cons_chars(s, r):
    assert longest_cons_char(s) == r
