# https://adventofcode.com/2022/day/8
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "inputs/advent_08_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['30373',
              '25512',
              '65332',
              '33549',
              '35390']
# endregion -------------------------
debug = True


class Tree:
    def __init__(self, height):
        self.height = height
        self.top = []
        self.right = []
        self.left = []
        self.bottom = []
        self._visible = False
        self._scenic_score = 1

    def is_visible(self):
        all_sides = [self.top, self.left, self.right, self.bottom]
        for i in all_sides:
            if max(i) < self.height:
                self._visible = True
        return self._visible

    def scenic_score(self):
        top = self.top.copy()
        left = self.left.copy()
        top.reverse()
        left.reverse()
        all_sides = [top, left, self.right, self.bottom]

        for i in all_sides:
            multiplier = 0
            for j in i:
                if j < self.height:
                    multiplier += 1
                else:
                    multiplier += 1
                    break
            self._scenic_score *= multiplier
        return self._scenic_score


def parse_input(my_input):
    trees = {}
    len_x = len(my_input[0])
    len_y = len(my_input)

    # create a dict of trees and their positions
    current_tree_x = 1
    current_tree_y = 1
    while current_tree_y < (len_y-1):
        while current_tree_x < (len_x-1):
            tree_height = int(my_input[current_tree_y][current_tree_x])
            trees[(current_tree_y, current_tree_x)] = Tree(tree_height)
            current_tree_x += 1
        current_tree_y += 1
        current_tree_x = 1

    # add trees to tree lists
    for ind, tree in trees.items():
        tree_y = ind[0]
        tree_x = ind[1]
        for i, line in enumerate(my_input):
            if i < tree_y:
                tree.top.append(int(line[tree_x]))
            elif i > tree_y:
                tree.bottom.append(int(line[tree_x]))
            else:
                for j, char in enumerate(line):
                    if j < tree_x:
                        tree.left.append(int(char))
                    elif j > tree_x:
                        tree.right.append(int(char))
    return trees


def part1(my_input):
    trees = parse_input(my_input)
    number_of_visible_trees = len(my_input)*2 + (len(my_input[0])-2)*2
    for tree in trees.values():
        if tree.is_visible():
            number_of_visible_trees += 1

    return number_of_visible_trees


def part2(my_input):
    trees = parse_input(my_input)
    scenic_scores = [tree.scenic_score() for tree in trees.values()]

    return max(scenic_scores)


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 1827
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 335580
