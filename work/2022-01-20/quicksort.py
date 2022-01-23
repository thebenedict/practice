#!/usr/bin/env python3

"""
    Quick sort
    Implement quick sort for a list of integers
"""


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
    output = quicksort(input)
    print(output)
    assert output == sorted(input)


def quicksort(input: list) -> list:
    return quicksort_helper(input, 0, len(input))


def quicksort_helper(input: list, lo: int, hi: int) -> list:
    if lo < hi:
        p = partition(input, lo, hi)
        quicksort_helper(input, lo, p)
        quicksort_helper(input, p + 1, hi)
    return input


def partition(input: list, lo: int, hi: int) -> int:
    p = input[lo]
    i = lo
    for j in range(lo + 1, hi):
        if input[j] <= p:
            i += 1
            input[i], input[j] = input[j], input[i]
    input[i], input[lo] = input[lo], input[i]
    return i


if __name__ == "__main__":
    main()