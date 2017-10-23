

import pytest

from problems.p13_find_duplicate_num_no_change_array import find_duplications


test_params = [
    ([], -1),
    ([1, 1], 1),
    ([1, 2, 3], -1),
    ([1, 2, 6, 4, 5, 3], -1),
    ([1, 1, 1, 2, 2, 2], 1),
    ([1, 2, 2, 6, 4, 5, 2], 2),
    ([1, 2, 2, 6, 4, 5, 6], 6),
    ([3, 2, 1, 3, 4, 5, 6, 7], 3),
    ([2, 3, 5, 4, 3, 2, 6, 7], 3),
]


@pytest.mark.parametrize('numbers, expected', test_params)
def test_find_dup(numbers, expected):
    assert find_duplications(numbers) == expected
