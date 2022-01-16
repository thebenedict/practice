#!/usr/bin/env python3

'''
Return a list of node discovery times for a DFS traversal of a simple,
unidrected graph
'''

def main():
    g = [[1,2], [0,3], [0,3], [1,4,5,2], [3,5], [3,4]]
    print(discovery_times(g))
    assert discovery_times(g) == [0, 1, 5, 2, 3, 4]

def discovery_times(g: list) -> list:
    return []

if __name__ == "__main__":
    main()