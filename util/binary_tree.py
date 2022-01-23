from __future__ import annotations
from typing import Optional

'''
Construct a binary tree from a list of integers
Note: Not a binary search tree

Use as:
root = BinaryTree([3,9,20,None,None,15,7]).root
'''
class Node:
    def __init__(self, val: int = None, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, values: list):
        if values:
            self.root = self.build_tree(0, values)

    def build_tree(self, idx: Optional[int], values: list) -> Node:
        if not values[idx]:
            return None
        r = Node(val = values[idx])
        left_index = 2 * idx + 1
        right_index = 2 * idx + 2
        if left_index < len(values):
            r.left = self.build_tree(left_index, values)
        if right_index < len(values):
            r.right = self.build_tree(right_index, values)
        return r
        