#!/usr/bin/env python3

"""
Given a simple undirected graph, return a list of articulation points

Challenge: LC 1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/
"""


def main():
    g = [[1, 2], [0, 3], [0, 3], [1, 4, 5, 2], [3, 5], [3, 4]]
    ap = articulation_points(g)
    print(ap)
    assert ap == [3]

    g = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3, 4]]
    ap = articulation_points(g)
    print(ap)
    assert ap == [1, 3]


def articulation_points(g: list) -> list:
    return []


if __name__ == "__main__":
    main()
