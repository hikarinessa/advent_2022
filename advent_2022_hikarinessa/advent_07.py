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
debug = False


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
            total_size += directory.get_total_size()
        self._total_size = total_size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def create_dictionary(my_input):
    files = {}
    directories = {'//': Directory('//')}

    active_dir = ''
    # process all the input into the files and directories dictionaries
    for i, line in enumerate(my_input):
        a_dir = re.match(r"dir ([a-z]+)", line)
        a_file = re.match(r"(\d+) ([a-z.]+)", line)
        new_active_dir = re.match(r"\$ cd ([a-z/]+)", line)
        go_back = re.match(r"\$ cd \.\.", line)
        if new_active_dir:
            active_dir += '/' + new_active_dir.group(1)
        elif go_back:
            dir_split = active_dir.rfind("/")
            active_dir = active_dir[:dir_split]
        elif a_dir:
            name = active_dir + '/' + a_dir.group(1)
            directories[name] = Directory(name)
            directories[active_dir].subdir.append(directories[name])
        elif a_file:
            size = a_file.group(1)
            name = a_file.group(2)
            files[name] = File(name, size)
            directories[active_dir].files.append(files[name])

    return directories


def part1(my_input):
    directories = create_dictionary(my_input)
    total_sum = 0

    for directory in directories:
        dir_size = directories[directory].get_total_size()
        if dir_size <= 100000:
            total_sum += dir_size

    if debug:
        for directory in directories.values():
            print(directory.name,
                  [file.name for file in directory.files],
                  [dire.name for dire in directory.subdir])

    return total_sum


def part2(my_input):
    directories = create_dictionary(my_input)
    my_dir_sizes = [size.get_total_size() for size in directories.values()]
    my_dir_sizes.sort()
    target_deletion = 40000000 - max(my_dir_sizes)
    for i in my_dir_sizes:
        if i + target_deletion > 0:
            return i


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 1348005
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 12785886
