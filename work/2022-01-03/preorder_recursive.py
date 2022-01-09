#!/usr/bin/env python3

'''
Print the preorder traversal of a binary tree -- use recursion

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

def preorder(root: Node, traversal):
    if root:
        traversal.append(root.val)
        preorder(root.left, traversal)
        preorder(root.right, traversal)
    return traversal

if __name__ == "__main__":
    main()