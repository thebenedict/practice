#!/usr/bin/env python3

"""
Return a list of all subsets of integers from 0..n
"""


def main():
    s = AllSubsets(3)
    print(s.subsets)
    assert sorted(s.subsets) == [[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]


class AllSubsets:
    def __init__(self, n: int):
        self.n = n
        self.subsets = []
        self.generate_all_subsets([], 0)

    def generate_all_subsets(self, soln: list, pos: int) -> None:
        pass
        # code here, solution goes in self.subsets


if __name__ == "__main__":
    main()
