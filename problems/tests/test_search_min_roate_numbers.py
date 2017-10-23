

import pytest

from problems.p23_search_min_in_roate_numbers import (search_min_num,
                                                      search_min_in_order)


test_params = [
    ([2], 2),
    ([3, 4, 5, 1, 2], 1),
    ([3, 4, 5, 1, 1, 2], 1),
    ([3, 4, 5, 1, 2, 2], 1),
    ([1, 0, 1, 1, 1], 0),
    ([1, 2, 3, 4, 5], 1)
]


@pytest.mark.parametrize('numbers, expected', test_params)
def test_search_min(numbers, expected):
    assert search_min_num(numbers) == expected
    # assert search_min_in_order(numbers) == expected
