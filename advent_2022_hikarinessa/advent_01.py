# https://adventofcode.com/2022/day/1
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_01_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['1000',
              '2000',
              '3000',
              '',
              '4000',
              '',
              '5000',
              '6000',
              '',
              '7000',
              '8000',
              '9000',
              '',
              '10000']
# endregion -------------------------
debug = False


def elves_load_list(my_input):
    elves_load = []
    temp_cal_amount = 0
    for ind, i in enumerate(my_input):
        if i == '':
            elves_load.append(temp_cal_amount)
            temp_cal_amount = 0
        elif ind+1 == len(my_input):
            temp_cal_amount += int(i)
            elves_load.append(temp_cal_amount)
        else:
            temp_cal_amount += int(i)

    if debug: print(elves_load)
    return elves_load


def part1(my_input):
    most_calories = max(elves_load_list(my_input))
    return most_calories


def part2(my_input):
    elves_load_sorted = elves_load_list(my_input)
    elves_load_sorted.sort()
    three_most_calories = elves_load_sorted.pop() + elves_load_sorted.pop() + elves_load_sorted.pop()
    return three_most_calories


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 64929
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 193697
