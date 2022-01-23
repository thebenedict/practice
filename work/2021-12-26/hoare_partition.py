#!/usr/bin/env python3

"""
    Hoare partition
    Partition an array using Hoare's partition scheme

    Note: Unlike Lumoto, in Hoare's partitioning the return value isn't necessarily the location
    of the pivot in the array. It is just the last index of the partition: at and below that index
    all elements are LTE some pivot value. The index returned from Hoare's partition does not tell you
    what partition value was used.
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
        14,
    ]
    pivot, partition_index = partition(input)
    for a in input[:partition_index]:
        assert a <= pivot
    for a in input[partition_index:]:
        assert a >= pivot


def partition(input: list) -> tuple([int, int]):
    pivot = input[0]
    print(pivot)
    j = len(input)
    i = -1

    while True:
        i += 1
        while input[i] < pivot:
            i += 1

        j -= 1
        while input[j] > pivot:
            j -= 1

        if i >= j:
            return pivot, j + 1

        input[i], input[j] = input[j], input[i]


if __name__ == "__main__":
    main()
