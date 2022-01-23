#!/usr/bin/env python3

"""
    Hoare partition
    Partition an array using Hoare's partition scheme

    Unlike Lumoto, in Hoare's partitioning, the return value is not necessarily the location
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
    output, p, pivot = partition(input)
    print(output)
    for a in output[:p]:
        assert a <= pivot
    for a in output[p + 1 :]:
        assert a > pivot


def partition(input):
    i = 0
    j = len(input) - 1

    pivot = input[(i + j) // 2]
    print(f"value of pivot: {pivot}")
    while True:
        while input[i] <= pivot:
            i += 1
        while input[j] >= pivot:
            j -= 1

        if i >= j:
            print(f"{i}, {j}, {input[i]}, {input[j]}")
            return input, j, pivot

        input[i], input[j] = input[j], input[i]


if __name__ == "__main__":
    main()
