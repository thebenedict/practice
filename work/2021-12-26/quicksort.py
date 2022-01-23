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
    quicksort(input)
    # print(p)
    print(input)
    assert input == sorted(input)


def quicksort(input: list) -> None:
    quicksort_helper(input, 0, len(input))


def quicksort_helper(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)
    quicksort_helper(arr, lo, p)
    quicksort_helper(arr, p + 1, hi)


def partition(arr, lo, hi):
    partition_val = arr[lo]
    i = lo
    for j in range(lo + 1, hi):
        if arr[j] <= partition_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[i] = arr[i], arr[lo]
    return i


if __name__ == "__main__":
    main()
