#!/usr/bin/env python3

"""
find the shortest path between A and D
"""


def main():
    g = {
        "H": ["G"],
        "G": ["C", "H"],
        "F": ["C"],
        "E": ["A", "B", "D"],
        "A": ["B", "E", "C"],
        "B": ["A", "D", "E"],
        "D": ["B", "E"],
        "C": ["A", "F", "G"],
    }

    assert shortest_path("A", "D", g) in [["A", "E", "D"], ["A", "B", "D"]]


def shortest_path(start: str, end: str, g: dict) -> list:
    return []


if __name__ == "__main__":
    main()
