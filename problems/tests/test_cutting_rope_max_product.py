
import pytest

from problems.p26_cutting_rope_max_product import (max_product_dynamic,
                                                   max_product_greedy)


test_params = [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 9),
    (7, 12),
    (8, 18),
    (9, 27),
    (10, 36),
    (50, 86093442),
]


@pytest.mark.parametrize('length, expected', test_params)
def test_max_product_dynamic(length, expected):
    assert max_product_dynamic(length) == expected
    assert max_product_greedy(length) == expected
