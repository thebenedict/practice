#!/usr/bin/env python3

"""
Return a list of all permutations of a list

Related to LC 797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


def main():
    s = AllPermutations([1, 2, 3])
    print(s.permutations)


class AllPermutations:
    def __init__(self, input: list):
        self.input = input
        self.permutations = []
        self.generate_all_permutations([], input)

    def generate_all_permutations(self, soln: list, candidates: list) -> None:
        pass
        # code here, soln in self.permutations


if __name__ == "__main__":
    main()
