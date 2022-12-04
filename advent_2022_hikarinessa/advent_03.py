# https://adventofcode.com/2022/day/3
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_03_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['vJrwpWtwJgWrhcsFMMfFFhFp',
              'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
              'PmmdzqPrVvPwwTWBwg',
              'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
              'ttgJtRGJQctTZtZT',
              'CrZsJsPPZsGzwwsLwLmpwMDw']
# endregion -------------------------
debug = False
item_value = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Rucksack:
    def __init__(self, items):
        self.items = items
        self.halflength = int(len(items)/2)
        self.compartment_one = items[:self.halflength]
        self.compartment_two = items[self.halflength:]
        self.duplicate_item = self.find_duplicate()
        self.dup_item_value = self.find_value()

    def find_duplicate(self):
        for i in self.compartment_one:
            if i in self.compartment_two:
                return i

    def find_value(self):
        return item_value.find(self.duplicate_item) + 1


def part1(my_input):
    total_value = 0
    for i in my_input:
        j = Rucksack(i)
        total_value += j.dup_item_value
    return total_value


def part2(my_input):
    my_input.reverse()
    total_value = 0
    iterations = int(len(my_input)/3)
    for i in range(0, iterations):
        x, y, z = my_input.pop(), my_input.pop(), my_input.pop()
        if debug: print(x, y, z)
        for j in x:
            if j in y:
                if j in z:
                    total_value += item_value.find(j) + 1
                    if debug: print(j)
                    break
    return total_value


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 8243
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 2631


