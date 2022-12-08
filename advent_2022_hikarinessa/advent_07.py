# https://adventofcode.com/2022/day/7
# region ---- imports and inputs ----
import os
import sys
import re

with open(os.path.join(sys.path[0], "inputs/advent_07_testinput.txt"), "r") as raw_input:
    TEST_INPUT = raw_input.read().splitlines()
with open(os.path.join(sys.path[0], "inputs/advent_07_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

# endregion -------------------------
debug = True


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdir = []
        self._total_size = 0

    def get_total_size(self):
        self.set_total_size()
        return self._total_size

    def set_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for directory in self.subdir:
            total_size += directory.total_size()
        self._total_size = total_size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def part1(my_input):
    files = {}
    directories = {'/': Directory('/')}
    active_dir = '/'
    for i, line in enumerate(my_input):
        a_dir = re.match(r"dir ([a-z]+)", line)
        a_file = re.match(r"(\d+) ([a-z.]+)", line)
        new_active_dir = re.match(r"\$ cd ([a-z./]+)", line)
        if new_active_dir:
            active_dir = new_active_dir.group(1)
        if a_dir:
            name = a_dir.group(1)
            bob = Directory(name)
            directories[name] = bob
            directories[active_dir].subdir.append(bob)
        elif a_file:
            size = a_file.group(1)
            name = a_file.group(2)
            files[name] = File(name, size)
            directories[active_dir].files.append(files[name])

    total_sum = 0
    for directory in directories:
        dir_size = directories[directory].get_total_size()
        if dir_size <= 100000:
            total_sum += dir_size

    if debug:
        for directory in directories.values():
            print(directory.name, [file.name for file in directory.files], [dire.name for dire in directory.subdir])
    return total_sum


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 1163150 too low
    print('*'*30)
    print('Part 2 =', )  #
