

import pytest

from problems.p25_robot_moving_count import robot_move_count

test_params = [
    ((10, 10, 5), 21),
    ((20, 20, 15), 359),
    ((1, 100, 10), 29),
    ((1, 10, 10), 10),
    ((100, 1, 15), 79),
    ((10, 1, 10), 10),
    ((1, 1, 15), 1),
    ((1, 1, 0), 1),
    ((-10, 10, 10), 0),
]


@pytest.mark.parametrize('numbers, expected', test_params)
def test_robot_move_count(numbers, expected):
    assert robot_move_count(*numbers) == expected
