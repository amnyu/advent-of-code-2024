from enum import Enum
from typing import List, Tuple

CoordType = Tuple[int, int]
lab_map = []
direction_indexes = "^>v<"
obstacle_char = "#"
visited_char = "X"
directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
    ".": (0,0)
}

def get_input(test_input: bool = True):
    global lab_map
    file_name = "test_input.txt" if test_input else "input.txt"
    with open(file_name, "r") as f:
        lab_map = f.read().splitlines()


def find_start() -> CoordType:
    for i, line in enumerate(lab_map):
        if (guard_index:= line.find("^")) > -1:
            return guard_index, i

    raise Exception("Guard not found")

def get_character_at_pos(x: int, y: int) -> str:
    return lab_map[y][x]

def set_character_at_pos(pos: CoordType, character: str):
    line_to_change = list(lab_map[pos[1]])
    line_to_change[pos[0]] = character
    lab_map[pos[1]] = "".join(line_to_change)

def sum_pos(first_pos: CoordType, second_pos: CoordType) -> CoordType:
    return first_pos[0] + second_pos[0], first_pos[1] + second_pos[1]

def is_inbound(position: CoordType) -> bool:
    return (
        0 <= position[0] < len(lab_map) and
        0 <= position[1] < len(lab_map[position[0]])
    )

def change_direction(direction: str) -> str:
    return direction_indexes[(direction_indexes.index(direction) + 1) % len(direction_indexes)]

def print_map():
    for line in lab_map:
        print(line)
    print("=" * len(line))

def move(guard_pos: CoordType):
    current_direction = get_character_at_pos(*guard_pos)
    visited = []
    if current_direction is None:
        raise Exception("Direction not found, {} found instead".format(current_direction))

    while True:
        visited.append(guard_pos)
        new_pos = sum_pos(guard_pos, directions[current_direction])
        # print_map()
        if is_inbound(new_pos):
            if get_character_at_pos(*new_pos) != obstacle_char:
                set_character_at_pos(guard_pos, visited_char)
                set_character_at_pos(new_pos, current_direction)
                guard_pos = new_pos
                continue
            else:
                current_direction = change_direction(current_direction)
        else:
            print("He's out!")
            print(len(set(visited)))
            print_map()
            return

    print(guard_pos)



if __name__ == '__main__':
    get_input(False)
    print(lab_map)
    move(find_start())