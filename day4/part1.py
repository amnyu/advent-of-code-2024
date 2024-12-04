from enum import Enum
from typing import Tuple, List


ex_input = """MMMSXXMASM
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


get_letter = lambda x, y: ex_input[y][x]
sum_coords = lambda x, y: (x[0] + y[0], x[1] + y[1])

visited_input = [["."] * len(x) for x in ex_input]
string_to_find = "XMAS"
found_words = []

Directions = Enum("Directions", "Up Dn Left Right LeftUp RightUp LeftDn RightDn")
directions = {
    Directions.Up: (0, -1),
    Directions.Dn: (0, 1),
    Directions.Left: (-1, 0),
    Directions.Right: (1, 0),
    Directions.LeftUp: (-1, -1),
    Directions.RightUp: (1, -1),
    Directions.LeftDn: (-1, 1),
    Directions.RightDn: (1, 1)
}


def find_all_starting_points() -> List[Tuple[int, int]]:
    pairs = []
    letter_to_find = string_to_find[0]
    for i, line in enumerate(ex_input):
        last_found = -1
        while (last_found := line.find(letter_to_find, last_found + 1)) >= 0:
            pairs.append((last_found, i))

    return pairs


def explore_for_words(starting_point: Tuple[int, int]) -> int:
    found_words = 0

    for direction in Directions:
        x = check_next_letter(0, starting_point, direction)
        if x != 0:
            visited_input[starting_point[1]][starting_point[0]] = get_letter(*starting_point)
        found_words += x
    return found_words


def check_next_letter(letter_idx: int, coord: Tuple[int, int], direction: Directions):
    coord = sum_coords(coord, directions[direction])
    letter_idx += 1

    if -1 < coord[1] < len(ex_input):
        if -1 < coord[0] < len(ex_input[coord[1]]):
            if get_letter(*coord) == string_to_find[letter_idx]:
                if letter_idx == len(string_to_find) - 1:
                    visited_input[coord[1]][coord[0]] = get_letter(*coord)
                    return 1
                x = check_next_letter(letter_idx, coord, direction)
                if x == 1:
                    visited_input[coord[1]][coord[0]] = get_letter(*coord)
                return x

    return 0


if __name__ == '__main__':
    starting_points = find_all_starting_points()
    result = []
    for starting_point in starting_points:
        result.append(explore_for_words(starting_point))

    print(sum(result))
