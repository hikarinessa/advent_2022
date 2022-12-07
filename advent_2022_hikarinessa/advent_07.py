# https://adventofcode.com/2022/day/7
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_07_testinput.txt"), "r") as raw_input:
    TEST_INPUT = raw_input.read().splitlines()
with open(os.path.join(sys.path[0], "inputs/advent_07_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

# endregion -------------------------
debug = True


class Directory:
    def __init__(self, name):
        self.name = ''
        self.files = []
        self.subdir = []

    def get_total_size(self):
        pass


if __name__ == "__main__":
    print('Part 1 =', )  #
    print('*'*30)
    print('Part 2 =', )  #
