#!/usr/bin/env python3

"""
Print the postorder traversal of a binary tree -- iterative approach

class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
"""

from binary_tree import BinaryTree, Node


def main():
    root = BinaryTree([3, 9, 20, None, None, 15, 7]).root
    traversal = postorder(root, [])
    print(traversal)
    assert traversal == [9, 15, 7, 20, 3]


"""
        3

    9      20

        15      7

3, 20, 15

# iterative dfs from the root
# append node.val to traversal after we traverse both l and r subtree

traversal, stack
node = root
keep going left, appending to stack
if stack
    node = pop
        if parent of node is at top of the stack, we just finished traversing right subtree
            append node to traversal
        else
            push node back onto stack, node = node.right
else
    return traversal
"""


def postorder(root: Node, traversal: list) -> list:
    traversal = []
    stack = []

    node = root
    while True:
        while node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            if stack and stack[-1] == node.right:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                traversal.append(node.val)
                node = None
        else:
            return traversal


if __name__ == "__main__":
    main()
