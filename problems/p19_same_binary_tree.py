# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p and q:
        is_left_same = is_same_tree(p.left, q.left)
        is_right_same = is_same_tree(p.right, q.right)
        return p.val == q.val and is_left_same and is_right_same
    else:
        return False


if __name__ == '__main__':
    tree1 = Node(3, left=Node(2), right=Node(1))
    tree2 = Node(3, left=Node(4), right=Node(1))
    tree3 = Node(3, left=Node(2), right=Node(1))
    print(is_same_tree(tree1, tree2))
    print(is_same_tree(tree1, tree3))
