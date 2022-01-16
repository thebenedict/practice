#!/usr/bin/env python3

'''
Given a simple undirected graph, return a list low, where low[n] is the
earliest discovery time reachable from node n by following one back edge
'''

def main():
    g = [[1,2], [0,3], [0,3], [1,4,5,2], [3,5], [3,4]]
    low = find_low(g)
    print(low)
    assert low == [0, 0, 0, 0, 2, 2]

def find_low(g: list) -> list:
    return []

if __name__ == "__main__":
    main()