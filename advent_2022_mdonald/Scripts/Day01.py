import os
import sys


INPUT_TXT = "../Input/Day01.txt"

class Elf():
    def __init__(self) -> None:
        self.inventory = []
    
    def get_total_inventory(self) -> int:
        return sum(self.inventory)
    
    def add_inventory_item(self, item) -> None:
        self.inventory.append(item)


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return txt.splitlines()


def do_magic():
    group_inventory = parse_input(get_input())
    elves = []
    elf = Elf()
    elves.append(elf)
    while len(group_inventory):
        item = group_inventory.pop()
        if item:
            elf.add_inventory_item(int(item))
        else:
            elf = Elf()
            elves.append(elf)
    
    elves.sort(key=lambda elf: elf.get_total_inventory())
    first, second, third = [elf.get_total_inventory() for elf in elves[-3:]]
    print("*"*96)
    print("* The top 3 elves are carrying:")
    print("* " + str(first))
    print("* " + str(second))
    print("* " + str(third))
    print("*")
    print("* With a total combined calorie count of " + str(first+second+third))


do_magic()
