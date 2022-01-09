#!/usr/bin/env python3

"""
    Lumoto partition
    Partition an array using Lumoto's partition scheme
"""

def main():
    input = [37, 13, 25, 26, 40, 5, 24, 10, 22, 10, 3, 28, 21, 14, 30, 21, 2, 31, 12, 23, 11, 17, 1, 31, 26, 12, 29, 14, 27, 32, 12, 23, 38, 32, 22, 18, 33, 14, 39, 38, 0, 33, 37, 10, 24, 38, 9, 13, 37, 14]
    output, p = partition(input)
    print(output)
    print(output[p])
    for a in output[:p - 1]:
        assert a <= output[p]
    for a in output[p + 1:]:
        assert a > output[p]

def partition(input):
    partition_val = input[-1]
    i = -1
    for j in range(len(input) - 1):
        if input[j] <= partition_val:
            i += 1
            input[i], input[j] = input[j], input[i]
    input[i + 1], input[-1] = input[-1], input[i + 1]
    return input, i + 1

if __name__ == "__main__":
    main()