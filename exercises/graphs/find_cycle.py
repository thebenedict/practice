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

def has_cycle(g):
    return True
    
if __name__ == "__main__":
    main()

