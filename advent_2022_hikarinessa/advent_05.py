# https://adventofcode.com/2022/day/5
# region ---- imports and inputs ----
import os
import sys
import re
import pprint

with open(os.path.join(sys.path[0], "inputs/advent_05_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['    [D]    ',
              '[N] [C]    ',
              '[Z] [M] [P]',
              ' 1   2   3 ',
              '',
              'move 1 from 2 to 1',
              'move 3 from 1 to 3',
              'move 2 from 2 to 1',
              'move 1 from 1 to 2']
# endregion -------------------------
debug = True


def parse_input(my_input):

    # First I'm going to separate the list of crates from the list of moves
    crates = []
    defining_crates = True
    while defining_crates:
        line = my_input.pop(0)
        if line == '':
            defining_crates = False
        else:
            string_temp = ''
            new_string = ''
            for i, char in enumerate(' ' + line):
                if i % 4 != 0:
                    string_temp += char
            for i, char in enumerate('  ' + string_temp):
                if i % 3 == 0:
                    new_string += char
            crates.append(new_string[1:])

    # now we're going to create a dictionary with the column numbers as keys
    # and a string of the crates on it, arranged bottom to top
    crates_dict = {}
    for i in crates.pop():
        crates_dict[int(i)] = ''
    while crates:
        line = crates.pop()
        for i in range(len(line)):
            if line[i] != ' ':
                crates_dict[i+1] += line[i]


    # finally we summarize each move into a list of 3 integers [crates to move, from, to]
    moves_list = [re.findall(r"\b\d+\b", i) for i in my_input]
    moves_list = [[int(i) for i in sublist] for sublist in moves_list]

    return crates_dict, moves_list


def magic(my_input):
    crates_dict_one, moves_list = parse_input(my_input.copy())
    crates_dict_two = crates_dict_one.copy()
    final_string_one = ''
    final_string_two = ''

    # perform all the moves
    for i in moves_list:
        x_nr = i[0]
        x_from = i[1]
        x_to = i[2]
        # part 1
        for j in range(0, x_nr):
            moved = crates_dict_one[x_from][-1:]
            crates_dict_one[x_from] = crates_dict_one[x_from][:-1]
            crates_dict_one[x_to] += moved
        # part 2
        moved = crates_dict_two[x_from][-x_nr:]
        crates_dict_two[x_from] = crates_dict_two[x_from][:-x_nr]
        crates_dict_two[x_to] += moved

    # collect the final strings
    for i in range(len(crates_dict_one)):
        final_string_one += crates_dict_one[i+1][-1:]
        final_string_two += crates_dict_two[i+1][-1:]

    return final_string_one, final_string_two


if __name__ == "__main__":
    print('Part 1 =', magic(INPUT)[0])  # VWLCWGSDQ
    print('*'*30)
    print('Part 2 =', magic(INPUT)[1])  # TCGLQSLPW
