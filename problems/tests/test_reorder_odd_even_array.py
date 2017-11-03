
import pytest

from problems.p37_reorder_odd_even_array import odd_even_reorder, odd_even_reorder1  # noqa


test_params = [
    ([1], [1]),
    ([2], [2]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7, 2, 4, 6]),
    ([2, 4, 6, 1, 3, 5, 7], [1, 3, 5, 7, 2, 4, 6]),
    ([1, 3, 5, 7, 2, 4, 6], [1, 3, 5, 7, 2, 4, 6]),
]


@pytest.mark.parametrize('array, expected', test_params)
def test_odd_even_array_reorder(array, expected):
    assert odd_even_reorder(array) == expected
    assert odd_even_reorder1(array) == expected
