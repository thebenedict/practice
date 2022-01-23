#!/usr/bin/env python3

"""
Determine if a simple, undirected graph is bipartite (eg. can it be colored
with two colors such that no edge links two same color verticies)

This is the same problem as LC 785 (medium)
https://leetcode.com/problems/is-graph-bipartite/
"""


def main():
    graphs = [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ([[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]], False),
        ([[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0]], True),
    ]

    for g, result in graphs:
        assert is_bipartite(g) == result


def is_bipartite(g: list) -> bool:
    return True


if __name__ == "__main__":
    main()
