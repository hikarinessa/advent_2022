# https://adventofcode.com/2022/day/9
# region ---- imports and inputs ----
import os
import sys
import math

with open(os.path.join(sys.path[0], "inputs/advent_09_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2']
TEST_INPUT2 = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']
# endregion -------------------------
debug = False


class End:
    def __init__(self):
        self.current_pos = [0,0]
        # self.move_pos = [(0, 0)]
        self.follow_pos = [(0, 0)]

    def _get_diff(self, head_pos):
        diff = []
        for x, y in zip(head_pos, self.current_pos):
            diff.append(x - y)
        return diff

    def is_move_needed(self, head_pos):
        diff = self._get_diff(head_pos)
        length = math.sqrt(sum(x**2 for x in diff))
        if length >= 2.0:
            return True
        else:
            return False

    def move(self, instruction):
        if instruction[:1] == 'R':
            self.current_pos[1] += 1
        if instruction[:1] == 'L':
            self.current_pos[1] -= 1
        if instruction[:1] == 'U':
            self.current_pos[0] -= 1
        if instruction[:1] == 'D':
            self.current_pos[0] += 1
        # self.move_pos.append(tuple(self.current_pos))

    def follow(self, head_pos):
        diff = self._get_diff(head_pos)
        if diff[0] == 0:
            self.current_pos[1] += int(math.copysign(1,diff[1]))
        elif diff[1] == 0:
            self.current_pos[0] += int(math.copysign(1,diff[0]))
        else:
            self.current_pos[0] += int(math.copysign(1,diff[0]))
            self.current_pos[1] += int(math.copysign(1,diff[1]))
        self.follow_pos.append(tuple(self.current_pos))


def part1(my_input):
    head = End()
    tail = End()
    for instruction in my_input:
        for i in range(0, int(instruction[2:])):
            head.move(instruction)
            if debug: print('move', tail.current_pos, head.current_pos)
            if tail.is_move_needed(head.current_pos):
                tail.follow(head.current_pos)
                if debug: print('follow', tail.current_pos, head.current_pos)
    num_positions = len(set(tail.follow_pos))
    return num_positions


def part2(my_input):
    head = End()
    seg1 = End()
    seg2 = End()
    seg3 = End()
    seg4 = End()
    seg5 = End()
    seg6 = End()
    seg7 = End()
    seg8 = End()
    tail = End()
    for instruction in my_input:
        for i in range(0, int(instruction[2:])):
            head.move(instruction)
            if seg1.is_move_needed(head.current_pos):
                seg1.follow(head.current_pos)
                if seg2.is_move_needed(seg1.current_pos):
                    seg2.follow(seg1.current_pos)
                    if seg3.is_move_needed(seg2.current_pos):
                        seg3.follow(seg2.current_pos)
                        if seg4.is_move_needed(seg3.current_pos):
                            seg4.follow(seg3.current_pos)
                            if seg5.is_move_needed(seg4.current_pos):
                                seg5.follow(seg4.current_pos)
                                if seg6.is_move_needed(seg5.current_pos):
                                    seg6.follow(seg5.current_pos)
                                    if seg7.is_move_needed(seg6.current_pos):
                                        seg7.follow(seg6.current_pos)
                                        if seg8.is_move_needed(seg7.current_pos):
                                            seg8.follow(seg7.current_pos)
                                            if tail.is_move_needed(seg8.current_pos):
                                                tail.follow(seg8.current_pos)
    num_positions = len(set(tail.follow_pos))
    return num_positions


if __name__ == "__main__":
    print('Part 1 =', part1(INPUT))  # 6256
    print('*'*30)
    print('Part 2 =', part2(INPUT))  # 2665
