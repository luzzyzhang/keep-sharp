# -*- coding: utf-8 -*-

import pytest

from problems.p45_stack_push_pop_order import is_pop_order


test_params = [
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [3, 5, 4, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([1, 2, 3, 4, 5], [3, 5, 4, 1, 2], False),
    ([1], [2], False)
]


@pytest.mark.parametrize('push_order, pop_order,  expected', test_params)
def test_is_pop_order(push_order, pop_order, expected):
    assert is_pop_order(push_order, pop_order) is expected
