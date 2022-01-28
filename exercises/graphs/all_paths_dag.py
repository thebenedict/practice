#!/usr/bin/env python3

"""
Find all paths from source to target in a DAG

note for drawing on paper:
horizontally from A -> G, with A, B, E, G along top
"""


def main():
    g = {
        "A": ["B", "C"],
        "B": ["E", "D"],
        "C": [],
        "D": ["E", "F", "H"],
        "E": ["F", "G"],
        "F": ["G", "H"],
        "G": [],
        "H": [],
    }
    paths = all_paths(g, "A", "F")
    print(sorted(paths))
    assert sorted(paths) == [list("ABDEF"), list("ABDF"), list("ABEF")]


def all_paths(g: dict, source: str, target: str) -> list:
    return []


if __name__ == "__main__":
    main()
