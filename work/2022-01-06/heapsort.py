#!/usr/bin/env python3

"""
    Heap sort
    Implement heap sort for a list of integers
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
    input_dup = input[:]
    output = heap_sort(input)
    print(output)
    assert output == sorted(input_dup)


def heap_sort(input: list) -> list:
    pass


if __name__ == "__main__":
    main()
