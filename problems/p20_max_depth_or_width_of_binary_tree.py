# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def maxdepth(root):
    if not root:
        return 0
    # left_depth = maxdepth(root.left)
    # right_depth = maxdepth(root.right)
    # return max(left_depth, right_depth) + 1
    # or just oneline code
    return max(maxdepth(root.left), maxdepth(root.right)) + 1


def maxwidth(root):
    ans = 0
    queue = [(root, 1)]

    while queue:
        ans = max(ans, queue[-1][1] - queue[0][1] + 1)
        cur_level = []
        for node, index in queue:
            if node.left is not None:
                cur_level.append((node.left, index*2))
            if node.right is not None:
                cur_level.append((node.right, index*2+1))
        queue = cur_level

    return ans


if __name__ == '__main__':
    nodel = Node(3, left=Node(7, Node(0)), right=Node(6))
    noder = Node(2, left=Node(5), right=Node(4))
    root = Node(1, left=nodel, right=noder)
    print(maxdepth(root))
    print(maxwidth(root))
