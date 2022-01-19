#!/usr/bin/env python3

'''
Count connected components in a simple, undirected graph
'''

def main():
    g = [
        [1, 2], [0], [0], [4], [3], [], [7, 8, 9], [8, 6, 9], [6, 7, 9], [6, 7, 8]
    ]

    print(count_connected_components(g))
    assert count_connected_components(g) == 4

def count_connected_components(g: list) -> int:
    return 0

if __name__ == "__main__":
    main()