
import pytest

from problems.p47_sequence_of_binary_search_tree import is_bst_post_order_sequence  # noqa


test_params = [
    ([4, 8, 6, 12, 16, 14, 10], True),
    ([4, 6, 7, 5], True),
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], True),
    ([7, 4, 6, 5], False),
    ([4, 6, 12, 8, 16, 14, 10], False)
]


@pytest.mark.parametrize('lst, expected', test_params)
def test_is_bst_post_order_sequence(lst, expected):
    assert is_bst_post_order_sequence(lst) is expected
