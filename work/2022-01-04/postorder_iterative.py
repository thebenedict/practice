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
    stack = []
    cur = root
    while True:
        while cur:
            if cur.right:
                stack.append(cur.right)
            stack.append(cur)
            cur = cur.left

        if stack:
            cur = stack.pop()
            if stack and stack[-1] == cur.right:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                traversal.append(cur.val)
                cur = None
        else:
            return traversal


if __name__ == "__main__":
    main()