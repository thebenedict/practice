#!/usr/bin/env python3

"""
Print the inorder traversal of a binary tree -- iterative approach

class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
"""

from binary_tree import BinaryTree, Node


def main():
    root = BinaryTree([3, 9, 20, None, None, 15, 7]).root
    traversal = inorder(root, [])
    print(traversal)
    assert traversal == [9, 3, 15, 20, 7]


# iterative dfs on tree
# while true
# push node to stack, traverse its left subtree
# pop a node off the stack, append its val to the traversal
# traverse its right subtree
"""
            3
        9       20

            15      17

traversal = 9 3 15 20 17
"""


def inorder(root: Node, traversal: list) -> list:
    traversal = []
    stack = []

    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            traversal.append(node.val)
            node = node.right
        else:
            return traversal
    return traversal


if __name__ == "__main__":
    main()
