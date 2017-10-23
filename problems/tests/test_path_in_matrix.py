

import pytest

from problems.p24_has_specify_path_in_matrix import has_path_in_matrix


matrix = [['a', 'b', 't', 'g'],
          ['c', 'f', 'c', 's'],
          ['j', 'd', 'e', 'h']]

path1 = 'bfce'
path2 = 'abfb'
path3 = 'afeh'

matrix_one_row = [['a', 'b', 'c']]
matrix_one_col = [['a'], ['b'], ['c']]
path = 'abc'

matrix_long = [['A', 'B', 'C', 'E', 'H', 'J', 'I', 'G'],
               ['S', 'F', 'C', 'S', 'L', 'O', 'P', 'Q'],
               ['A', 'D', 'E', 'E', 'M', 'N', 'O', 'E'],
               ['A', 'D', 'I', 'D', 'E', 'J', 'F', 'M'],
               ['V', 'C', 'E', 'I', 'F', 'G', 'G', 'S']]
path_long = 'SLHECCEIDEJFGGFIE'

test_params = [
    ([], '', False),
    (matrix, path1, True),
    (matrix, path2, False),
    (matrix, path3, False),
    (matrix_one_row, path, True),
    (matrix_one_col, path, True),
    (matrix_long, path_long, True)
]


@pytest.mark.parametrize('matrix, path, expected', test_params)
def test_path_in_matrix(matrix, path, expected):
    assert has_path_in_matrix(matrix, path) is expected
