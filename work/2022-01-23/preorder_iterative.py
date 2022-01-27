#!/usr/bin/env python3

"""
Print the preorder traversal of a binary tree -- iterative approach

class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
"""

from binary_tree import BinaryTree, Node


def main():
    root = BinaryTree([3, 9, 20, None, None, 15, 7]).root
    traversal = preorder(root, [])
    print(traversal)
    assert traversal == [3, 9, 20, 15, 7]


def preorder(root: Node, traversal: list) -> list:
    traversal = []
    stack = []
    node = root

    while True:
        if node:
            traversal.append(node.val)
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            node = node.right
        else:
            return traversal


if __name__ == "__main__":
    main()
