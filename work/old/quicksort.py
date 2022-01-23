#!/usr/bin/env python3

"""
    Quick sort
    Implement quick sort for a list of integers
"""

import random


def main():
    input = [
        37,
        13,
        25,
        26,
        40,
        5,
        24,
        10,
        22,
        10,
        3,
        28,
        21,
        14,
        30,
        21,
        2,
        31,
        12,
        23,
        11,
        17,
        1,
        31,
        26,
        12,
        29,
        14,
        27,
        32,
        12,
        23,
        38,
        32,
        22,
        18,
        33,
        14,
        39,
        38,
        0,
        33,
        37,
        10,
        24,
        38,
        9,
        13,
        37,
        0,
    ]
    # input = [8, 1, 8, 5, 7, 3, 2, 0, 4]
    quicksort(input, 0, len(input) - 1)
    print(input)
    assert input == sorted(input)


def quicksort(input, low, high):
    if low < high:
        p = partition(input, low, high)
        quicksort(input, low, p - 1)
        quicksort(input, p + 1, high)


def partition(input, low, high):
    pivot_val = input[high]
    i = low - 1
    for j in range(low, high):
        if input[j] <= pivot_val:
            i += 1
            input[i], input[j] = input[j], input[i]
    input[high], input[i + 1] = input[i + 1], input[high]
    return i + 1


if __name__ == "__main__":
    main()
