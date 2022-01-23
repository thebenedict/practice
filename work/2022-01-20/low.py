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
    timer = [0]
    parent = [-1] * len(g)
    discovery_time = [-1] * len(g)
    low = [-1] * len(g)

    dfs(g, 0, parent, timer, discovery_time, low)
    return low

def dfs(g: list, node: int, parent: list, timer: list, discovery_time: list, low: list) -> None:
    discovery_time[node] = timer[0]
    low[node] = timer[0]
    timer[0] += 1
    for neighbor in g[node]:
        if discovery_time[neighbor] < 0:
            parent[neighbor] = node
            dfs(g, neighbor, parent, timer, discovery_time, low)
            low[node] = min([low[node], low[neighbor]]) 
        elif parent[neighbor] != node:
            low[node] = min([low[node], discovery_time[neighbor]])

if __name__ == "__main__":
    main()