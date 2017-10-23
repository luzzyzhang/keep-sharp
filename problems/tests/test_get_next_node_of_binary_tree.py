

import pytest

from problems.p18_get_binary_tree_next_node import get_next, Node


# Tree nodes
A, B, C = Node('a'), Node('b'), Node('c')
D, E, F = Node('d'), Node('e'), Node('f')
G, H, I = Node('g'), Node('h'), Node('i')

A.left, A.right = B, C
B.left, B.right, B.parent = D, E, A
C.left, C.right, C.parent = F, G, A
D.parent = B
E.left, E.right, E.parent = H, I, B
F.parent = C
G.parent = C
H.parent = E
I.parent = E

# In-order 中序遍历获得的序列
in_order = [D, B, H, E, I, A, F, C, G]

# 输入节点对应的下个节点
test_params = [
    (A, F),
    (D, B),
    (C, G),
    (E, I)
]


@pytest.mark.parametrize('node, expected', test_params)
def test_get_next_node(node, expected):
    assert get_next(node) == expected
