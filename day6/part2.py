from copy import deepcopy
from enum import Enum
from typing import List, Tuple, Union
import threading

CoordType = Tuple[int, int]

og_lab_map = []
lab_map = []
direction_indexes = "^>v<"
obstacle_char = "#"
extra_obstacle_char = "o"
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
    global og_lab_map
    file_name = "test_input.txt" if test_input else "input.txt"
    with open(file_name, "r") as f:
        lab_map = f.read().splitlines()

    og_lab_map = deepcopy(lab_map)


def find_start() -> CoordType:
    for i, line in enumerate(lab_map):
        if (guard_index:= line.find("^")) > -1:
            return guard_index, i

    raise Exception("Guard not found")

def get_character_at_pos(x: int, y: int, current_map: List[str] = None) -> str:
    if current_map is None:
        current_map = lab_map
    return current_map[y][x]

def set_character_at_pos(pos: CoordType, character: str, current_map: List[str] = None):
    if current_map is None:
        current_map = lab_map
    line_to_change = list(current_map[pos[1]])
    line_to_change[pos[0]] = character
    current_map[pos[1]] = "".join(line_to_change)
    return current_map

def sum_pos(first_pos: CoordType, second_pos: CoordType) -> CoordType:
    return first_pos[0] + second_pos[0], first_pos[1] + second_pos[1]

def is_inbound(position: CoordType) -> bool:
    return (
        0 <= position[0] < len(lab_map) and
        0 <= position[1] < len(lab_map[position[0]])
    )

def change_direction(direction: str) -> str:
    return direction_indexes[(direction_indexes.index(direction) + 1) % len(direction_indexes)]

def print_map(current_map: List[str] = None):
    if current_map is None:
        current_map = lab_map
    for line in current_map:
        print(line)
    print("=" * len(line))

def insert_obstacle(pos: CoordType, current_map: List[str] = None):
    global lab_map
    if current_map is None:
        current_map = lab_map
        lab_map = deepcopy(og_lab_map)

    set_character_at_pos(pos, extra_obstacle_char, current_map)
    return current_map

def move(guard_pos: CoordType, verify_loop: bool = False, current_map: List[str] = None) -> Union[List[CoordType], bool]:
    if current_map is None:
        current_map = lab_map

    current_direction = get_character_at_pos(*guard_pos, current_map)
    visited = []

    if current_direction is None:
        raise Exception("Direction not found, {} found instead".format(current_direction))

    while True:
        if not verify_loop:
            visited.append(guard_pos)
        else:
            visited.append(guard_pos + (current_direction,))
        new_pos = sum_pos(guard_pos, directions[current_direction])
        # print_map()
        if is_inbound(new_pos):
            if get_character_at_pos(*new_pos, current_map) not in [obstacle_char, extra_obstacle_char]:
                if verify_loop and new_pos + (current_direction, ) in visited:
                    print("Guard loops!")
                    return True

                set_character_at_pos(guard_pos, visited_char, current_map)
                set_character_at_pos(new_pos, current_direction, current_map)
                guard_pos = new_pos
                continue
            else:
                current_direction = change_direction(current_direction)
        else:
            print("He's out!")
            # print(len(set(visited)))
            # print_map(current_map)
            return visited if not verify_loop else False

    print(guard_pos)



if __name__ == '__main__':
    get_input(False)
    print(lab_map)
    guard_start_pos = find_start()
    possible_obstacles = move(guard_start_pos)
    result = []

    threads = []
    for i, obstacle_pos in enumerate(set(possible_obstacles)):
        if obstacle_pos == guard_start_pos:
            continue
        iter_map = deepcopy(og_lab_map)
        print("Iter {}: ".format(i), end="")
        iter_map = insert_obstacle(obstacle_pos, iter_map)
        result.append(move(guard_start_pos, verify_loop=True, current_map=iter_map))

    print("There are {} possible obstacles to make guard loop".format(len([x for x in result if x == True])))