
import pytest

from problems.p12_duplicate_number_in_array import duplicate2


empty = set()

test_params = [
    ([], empty),
    ([1, 1, 1, 2, 2, 2], {1, 2}),
    ([-1, 0], empty),
    ([7, 8, 9, 9], empty),
    ([2, 3, 1, 0, 2, 5, 3], {2, 3}),
    ([2, 1, 3, 1, 4], {1}),
    ([2, 4, 3, 1, 4], {4}),
    ([2, 4, 2, 1, 4], {2, 4}),
    ([0, 1, 2, 3, 3], {3}),
    ([0, 1, 2, 3], empty),
    ([2, 1, 3, 0, 4], empty)
]


@pytest.mark.parametrize('numbers, expected', test_params)
def test_duplicate(numbers, expected):
    assert set(duplicate2(numbers, len(numbers))) == expected
