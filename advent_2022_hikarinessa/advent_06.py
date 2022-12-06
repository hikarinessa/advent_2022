# https://adventofcode.com/2022/day/6
# region ---- imports and inputs ----
import os
import sys
import re

with open(os.path.join(sys.path[0], "inputs/advent_06_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',     # 7
              'bvwbjplbgvbhsrlpgdmjqwftvncz',       # 5
              'nppdvjthqldpwncqszvftbrmjlhg',       # 6
              'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',  # 10
              'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']   # 11
# endregion -------------------------
debug = True


def is_unique(my_input):
    return re.match(r"^(?!.*(.).*\1)[a-z]+$", my_input)


def magic(my_input, num):
    a = 0
    b = num
    while b <= len(my_input):
        my_string = my_input[a:b]
        if is_unique(my_string):
            return b
        a += 1
        b += 1


if __name__ == "__main__":
    print('Part 1 =', magic(INPUT[0], 4))  # 1625
    print('*'*30)
    print('Part 2 =', magic(INPUT[0], 14))  # 2250
