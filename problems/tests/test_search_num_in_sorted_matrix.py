

import pytest

from problems.p14_search_num_in_sorted_matrix import search_in_sorted_matrix

test_params = [
    ([], 1, False),
    ([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 7, True),
    ([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 15, True),
    ([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 1, True),
    ([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 99, False),
    ([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 5, False),
]


@pytest.mark.parametrize('matrix, target,  expected', test_params)
def test_search_sorted_matrix(matrix, target, expected):
    assert search_in_sorted_matrix(matrix, target) is expected
