#!/usr/bin/env python3

"""
Determine if a simple, undirected graph has a cycle
"""


def main():
    graphs = [
        ([[1, 4, 5], [0, 2], [1, 3], [2, 4], [0, 3], [0]], True),
        ([[1, 4, 5], [0, 2, 3], [1], [1], [0], [0]], False),
    ]

    for g, result in graphs:
        out = has_cycle(g)
        print(g, out)
        assert out == result


def has_cycle(g):
    discovered = set()
    parent = [-1] * len(g)
    return dfs(g, 0, parent, discovered)


def dfs(g: list, node: int, parent: list, discovered: set) -> bool:
    discovered.add(node)
    for neighbor in g[node]:
        if neighbor in discovered:
            if parent[node] != neighbor:
                return True
        else:
            parent[neighbor] = node
            if dfs(g, neighbor, parent, discovered):
                return True
    return False


if __name__ == "__main__":
    main()
