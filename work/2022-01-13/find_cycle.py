#!/usr/bin/env python3

'''
Determine if a simple, undirected graph has a cycle
'''

def main():
    graphs = [
        ([[1,4,5],[0,2],[1,3],[2,4],[0,3],[0]], True),
        ([[1,4,5],[0,2,3],[1],[1],[0],[0]], False)
    ]

    for g, result in graphs:
        out = has_cycle(g)
        print(g, out)
        assert out == result

'''
DFS traversal of the graph, marking nodes discovered and assigning parents to all
nodes except the root (start node). If we encounter a discovered neighbor, and 
that neighbor is not the parent of the current node, we have a cycle.
'''

def has_cycle(g: list) -> bool:
    discovered = set()
    parent = [-1] * len(g)
    return dfs(g, 0, discovered, parent)

def dfs(g: list, node: int, discovered: set, parent: list) -> bool:
    discovered.add(node)
    for neighbor in g[node]:
        if neighbor in discovered:
            if parent[node] != neighbor:
                return True
        else:
            parent[neighbor] = node
            if dfs(g, neighbor, discovered, parent):
                return True
    return False

if __name__ == "__main__":
    main()

