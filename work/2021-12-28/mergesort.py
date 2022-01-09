#!/usr/bin/env python3

"""
    Merge sort
    Implement merge sort for a list of integers
"""

def main():
    input = [37, 13, 25, 26, 40, 5, 24, 10, 22, 10, 3, 28, 21, 14, 30, 21, 2, 31, 12, 23, 11, 17, 1, 31, 26, 12, 29, 14, 27, 32, 12, 23, 38, 32, 22, 18, 33, 14, 39, 38, 0, 33, 37, 10, 24, 38, 9, 13, 37, 0]
    output = mergesort(input)
    print(output)
    assert output == sorted(input)

def mergesort(input: list) -> list:
    if len(input) <= 1:
        return input
    mid = len(input) // 2
    l = mergesort(input[:mid])
    r = mergesort(input[mid:])
    return merge(l, r)

def merge(l, r):
    out = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
            if l[i] < r[j]:
                out.append(l[i])
                i += 1
            else:
                out.append(r[j])
                j += 1
    while i < len(l):
        out.append(l[i])
        i += 1
    while j < len(r):
        out.append(r[j])
        j += 1
    return out

if __name__ == "__main__":
    main()
