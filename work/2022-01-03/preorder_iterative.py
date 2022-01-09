#!/usr/bin/env python3

'''
Print the preorder traversal of a binary tree -- iterative approach

class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
'''

from binary_tree import BinaryTree, Node

def main():
    root = BinaryTree([3,9,20,None,None,15,7]).root
    traversal = preorder(root, [])
    print(traversal)
    assert traversal == [3, 9, 20, 15, 7]

def preorder(root: Node, traversal: list) -> list:
    stack = [root]
    while stack:
        current = stack.pop()
        traversal.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return traversal

if __name__ == "__main__":
    main()