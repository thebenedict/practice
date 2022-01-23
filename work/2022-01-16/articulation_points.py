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
    assert sorted(ap) == [1, 3]


def articulation_points(g: list) -> list:
    parent = [-1] * len(g)
    discovery_time = [-1] * len(g)
    low = [-1] * len(g)
    timer = [0]
    ap = []

    dfs(g, 0, timer, parent, discovery_time, low, ap)
    return ap


def dfs(
    g: list,
    node: int,
    timer: list,
    parent: list,
    discovery_time: list,
    low: list,
    ap: list,
) -> None:

    discovery_time[node] = timer[0]
    low[node] = timer[0]
    timer[0] += 1
    for neighbor in g[node]:
        if discovery_time[neighbor] < 0:
            parent[neighbor] = node
            dfs(g, neighbor, timer, parent, discovery_time, low, ap)
            low[node] = min([low[node], low[neighbor]])
            if low[node] < low[neighbor]:
                ap.append(node)
        elif parent[neighbor] != node:
            low[node] = min([low[node], discovery_time[neighbor]])


if __name__ == "__main__":
    main()
