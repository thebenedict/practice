#!/usr/bin/env python3

'''
Print the postorder traversal of a binary tree -- iterative approach

class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
'''

from binary_tree import BinaryTree, Node

def main():
    root = BinaryTree([3,9,20,None,None,15,7]).root
    traversal = postorder(root, [])
    print(traversal)
    assert traversal == [9, 15, 7, 20, 3]

def postorder(root: Node, traversal: list) -> list:    
    return traversal

if __name__ == "__main__":
    main()