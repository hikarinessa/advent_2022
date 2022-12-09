# https://adventofcode.com/2022/day/2
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_02_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['A Y',
              'B X',
              'C Z']
# endregion -------------------------
debug = True


def translate_input(my_input):
    output = []
    temp_pair = []
    for i in my_input:
        for j in i:
            if j == 'A' or j == 'X':
                temp_pair.append(1)
            elif j == 'B' or j == 'Y':
                temp_pair.append(2)
            elif j == 'C' or j == 'Z':
                temp_pair.append(3)
            else:
                pass
        output.append(temp_pair)
        temp_pair = []
    return output


def part1(my_input):
    my_score = 0
    my_list = translate_input(my_input)
    for i in my_list:
        if i[0]-i[1] == -2 or i[0]-i[1] == 1:
            my_score += i[1]
        elif i[0]-i[1] == 0:
            my_score += i[1] + 3
        else:
            my_score += i[1] + 6
    return my_score


def part2(my_input):
    win_dict = {'A': 8, 'B': 9, 'C': 7}
    lose_dict = {'A': 3, 'B': 1, 'C': 2}
    draw_dict = {'A': 4, 'B': 5, 'C': 6}
    my_score = 0

    for i in my_input:
        if i[2] == 'X':
            my_score += lose_dict[i[0]]
        elif i[2] == 'Y':
            my_score += draw_dict[i[0]]
        elif i[2] == 'Z':
            my_score += win_dict[i[0]]
    return my_score


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 10994
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 12526
