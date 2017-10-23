
import pytest

from problems.p03_fill_water import (compute_filled_grids,
                                     compute_grids_with_stack)


matrix0 = [[3, 2, 5], [1, 4, 6], [7, 8, 9]]
matrix1 = [[6, 4, 3], [7, 2, 1], [5, 8, 9]]
matrix2 = [[0, 4, 3], [7, 2, 1], [5, 8, 9]]
matrix3 = [[6, 4, 3], [5, 2, 4], [8, 7, 9]]
matrix4 = [[6, 4, 3], [5, 7, 9], [2, 1, 8]]
matrix5 = [[6, 4, 2, 10], [7, 3, 8, 11], [5, 1, 9, 12]]
matrix6 = [[9, 8, 7], [11, 12, 6], [3, 4, 5], [1, 2, 10]]
matrix7 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


test_params = [
    (matrix0, 3),
    (matrix1, 5),
    (matrix2, 1),
    (matrix3, 5),
    (matrix4, 6),
    (matrix5, 5),
    (matrix6, 9),
    (matrix7, 9),
]


@pytest.mark.parametrize('matrix, expected', test_params)
def test_fill_water(matrix, expected):
    assert compute_filled_grids(matrix) == expected
    assert compute_grids_with_stack(matrix) == expected
