from enum import Enum
from typing import List, Tuple

ex_input_test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

with open("input.txt", "r") as f:
    ex_input = f.read().splitlines()


string_to_find = "MAS"
visited_input = [["."] * len(x) for x in ex_input]
get_letter = lambda x, y: ex_input[y][x]
sum_coords = lambda x, y: (x[0] + y[0], x[1] + y[1])

Directions = Enum("Directions", "LeftUp RightUp LeftDn RightDn")
directions = {
    Directions.LeftUp: (-1, -1),
    Directions.RightUp: (1, -1),
    Directions.LeftDn: (-1, 1),
    Directions.RightDn: (1, 1)
}


def mark_x_visited(x_point: Tuple[int, int]):
    for i in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]:
        coord = sum_coords(x_point, i)
        visited_input[coord[1]][coord[0]] = get_letter(*coord)

def print_visited():
    [print("".join(x)) for x in visited_input]


def find_all_starting_points() -> List[Tuple[int, int]]:
    pairs = []
    letter_to_find = string_to_find[1]
    for i, line in enumerate(ex_input):
        if i == 0 or i == len(ex_input):
            continue
        last_found = 0
        while (last_found := line.find(letter_to_find, last_found + 1)) >= 1 and last_found != len(line) - 1:
            pairs.append((last_found, i))

    return pairs


def check_next_letter(letter_idx: int, coord: Tuple[int, int], direction: Directions):
    if -1 < coord[1] < len(ex_input):
        if -1 < coord[0] < len(ex_input[coord[1]]):
            if get_letter(*coord) == string_to_find[letter_idx]:
                if letter_idx == len(string_to_find) - 1:
                    return 1
                return check_next_letter(letter_idx+1, sum_coords(coord, directions[direction]), direction)

    return 0

def verify_x_mas_at_point(a_point: Tuple[int, int]) -> bool:
    result = []
    # We've got a point, we need to check one axis if there's a MAS word:
    # first let's go with the leftup to rightdn
    axis1 = [Directions.LeftUp, Directions.RightDn]
    # now leftdn to rightup
    axis2 = [Directions.LeftDn, Directions.RightUp]

    # now compiling those
    for start_offset, direction in [axis1, axis2]:
        right_to_left = check_next_letter(0, sum_coords(a_point, directions[start_offset]), direction)
        left_to_right = check_next_letter(0, sum_coords(a_point, directions[direction]), start_offset)

        result.append(right_to_left or left_to_right)

    if all(result):
        # copy X to visited
        mark_x_visited(point)

    return all(result)


if __name__ == '__main__':
    starting_points = find_all_starting_points()
    results = []
    for point in starting_points:
        results.append(verify_x_mas_at_point(point))

    print_visited()
    print(sum(results))

