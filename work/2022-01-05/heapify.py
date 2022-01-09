#!/usr/bin/env python3

"""
    Heapify
    Build a min heap from an array of integers, without using heapq or similar
"""

def main():
    input = [1918, 2001, 1776, 1804, 1865, 1945, 1941, 1963, 1783, 1492]
    heapify(input)
    print(input)
    assert validate_heap(input)

def heapify(input: list) -> None:
    for i in range(len(input)):
        parent_idx = heap_parent(input, i)
        if parent_idx and input[i] < input[parent_idx]:
            bubble_up(input, i)

def heap_parent(input: list, i: int) -> int:
    if i == 0:
        return None
    return (i - 1) // 2

def bubble_up(input: list, i: int) -> None:
    parent_idx = heap_parent(input, i)
    if parent_idx is not None and input[i] < input[parent_idx]:
        input[i], input[parent_idx] = input[parent_idx], input[i]
        bubble_up(input, parent_idx)

# leave this collapesd while working
def validate_heap(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[(i - 1) // 2] > arr[i]: 
            return False
    return True

if __name__ == "__main__":
    main()
