# -*- coding: utf-8 -*-
"""
    序列化二叉树
    ~~~~~~~~~~~~
    请实现两个函数，分别用来序列化和反序列化二叉树。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root, stream):
    if root is None:
        stream.write('$'+',')
        return None
    stream.write(str(root.val) + ',')
    serialize(root.left, stream)
    serialize(root.right, stream)


def read_stream(stream, numbers):

    if not stream:
        return False
    numbers = [line.replace(',', ' ').replace('$', ' ').split() for line in stream]
    return [int(n) for number in numbers for n in number]


def deserialize(root, stream):
    if not stream:
        return []
    numbers = [line.replace(',', ' ').replace('$', ' ').split() for line in stream]
    numbers = [int(n) for number in numbers for n in number]
    if numbers:
        root.val = numbers[0]

        deserialize(root.left, stream)
        deserialize(root.right, stream)


if __name__ == '__main__':
    node1, node2, node3 = Node(1), Node(2), Node(3)
    node1.left, node1.right = node2, node3
    # with open('test.txt', 'w') as f:
    #     serialize(node1, f)
    root = Node(None)
    with open('test.txt', 'r') as f:
        # print(read_stream(f, []))
        deserialize(root, f)
    print(root.val, root.left, root.right)
