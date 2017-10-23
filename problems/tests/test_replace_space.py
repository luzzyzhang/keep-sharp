

import pytest

from problems.p15_replace_blanks_in_string import replace_space, replace_space2


test_params = [
    ('', ''),
    (' ', '%20'),
    ('   ', '%20%20%20'),
    ('HelloNiMaBiDeKitty', 'HelloNiMaBiDeKitty'),
    ('We are happy.', 'We%20are%20happy.'),
    ('We  arehappy.', 'We%20%20arehappy.'),
    (' HelloWorld', '%20HelloWorld'),
    ('HelloWorld ', 'HelloWorld%20'),
]


@pytest.mark.parametrize('string, expected', test_params)
def test_replace_space(string, expected):
    assert replace_space(string, 50) == expected
    assert replace_space2(string) == expected
