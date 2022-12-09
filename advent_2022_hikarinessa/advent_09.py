# https://adventofcode.com/2022/day/5
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_05_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

BOARD = ['......',
         '......',
         '......',
         '......',
         'H.....']
TEST_INPUT = ['R 4',
              'U 4',
              'L 3',
              'D 1',
              'R 4',
              'D 1',
              'L 5',
              'R 2']
# endregion -------------------------
debug = True


if __name__ == "__main__":
    print('Part 1 =', )  #
    print('*'*30)
    print('Part 2 =', )  #
