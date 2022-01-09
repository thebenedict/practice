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
    pass

# leave this collapesd while working
def validate_heap(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[(i - 1) // 2] > arr[i]: 
            return False
    return True

if __name__ == "__main__":
    main()
