#!/usr/bin/env python3

"""
    Merge sort
    Implement merge sort for a list of integers
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
    try:
        assert mergesort(input) == sorted(input)
        print("Sorted")
    except:
        print("Nope")
        print(mergesort(input))


def mergesort(input):
    if len(input) <= 1:
        return input
    mid = len(input) // 2
    l1 = input[0:mid]
    l2 = input[mid:]
    return merge(mergesort(l1), mergesort(l2))


def merge(l1, l2):
    out = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            out.append(l1[i])
            i += 1
        else:
            out.append(l2[j])
            j += 1
    while i < len(l1):
        out.append(l1[i])
        i += 1
    while j < len(l2):
        out.append(l2[j])
        j += 1
    return out


if __name__ == "__main__":
    main()
