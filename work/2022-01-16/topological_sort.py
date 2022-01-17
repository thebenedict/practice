#!/usr/bin/env python3

'''
Find a topological sort for a directed, acyclic graph
'''

def main():
    # example from Skiena 2e fig 5.15, p179
    g = {
        "A": ["B", "C"],
        "B": ["D", "C"],
        "C": ["E", "F"],
        "D": [],
        "E": ["D"],
        "F": ["E"],
        "G": ["A", "F"],
    }
    ts = topological_sort(g)
    print(ts)
    assert ts == list("GABCFED")

def topological_sort(g: dict) -> list:
    return []

if __name__ == "__main__":
    main()