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
        self.subsets.append(soln[:])
        for i in range(pos, self.n):
            soln.append(i)
            self.generate_all_subsets(soln, i + 1)
            soln.pop()


if __name__ == "__main__":
    main()
