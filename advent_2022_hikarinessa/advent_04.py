# https://adventofcode.com/2022/day/4
# region ---- imports and inputs ----
import os
import sys
import re

with open(os.path.join(sys.path[0], "inputs/advent_04_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['2-4,6-8',
              '2-3,4-5',
              '5-7,7-9',
              '2-8,3-7',
              '6-6,4-6',
              '2-6,4-8']
# endregion -------------------------
debug = True


def prep_input(my_input):
    my_list = [re.findall(r"\b\d+\b", i) for i in my_input]
    return [[int(i) for i in sublist] for sublist in my_list]


def part1(my_input):
    prepped_input = prep_input(my_input)
    nr_contained = 0
    for i in prepped_input:
        if i[3] >= i[0] >= i[2] and i[2] <= i[1] <= i[3]:
            nr_contained += 1
        elif i[1] >= i[2] >= i[0] and i[0] <= i[3] <= i[1]:
            nr_contained += 1
    return nr_contained


def part2(my_input):
    prepped_input = prep_input(my_input)
    not_contained = 0
    for i in prepped_input:
        if i[0] > i[3] or i[2] > i[1]:
            not_contained += 1
    return 1000 - not_contained


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 500
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 815
