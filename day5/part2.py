from collections import defaultdict
from typing import List, Tuple, Dict

str_list_to_int_list = lambda x: list(map(int, x))

def get_input(test_input: bool = True):
    file_name = "test_input.txt" if test_input else "input.txt"
    with open(file_name, "r") as f:
        return f.read().splitlines()

def parse_input(test_input: List[str]) -> Tuple[Dict[int, List[int]], List[List[int]]]:
    rules = []
    pages = []
    rules_flag = True

    for line in test_input:
        if rules_flag and len(split_rule:= line.split("|")) != 2:
            rules_flag = False
            continue  # it happens only on the empty line

        if rules_flag:
            rules.append(str_list_to_int_list(split_rule))
        else:
            pages_split = line.split(",")
            pages.append(str_list_to_int_list(pages_split))

    rules_dict = defaultdict(list)

    for rule in rules:
        rules_dict[rule[0]] += [rule[1]]

    return rules_dict, pages

def check_rules_per_update(update_row: List[int], rules: Dict[int, List[int]]) -> int:
    # returns middle page number if success, otherwise 0
    fixed = False
    while True:
        result = True
        for first, later_list in rules.items():
            for later in later_list:
                if first in update_row and later in update_row:
                    if (i:=update_row.index(first)) > (j:=update_row.index(later)):
                        result = False
                        fixed = True
                        update_row[i], update_row[j] = update_row[j], update_row[i]
                        print(f"Swapped {update_row[i]} {update_row[j]}")
                        if not result:
                            break
            if not result:
                break
        if result:
            break

    if fixed:
        return update_row[len(update_row) // 2]
    else:
        return 0


if __name__ == '__main__':
    raw_input = get_input(False)
    page_ordering, pages_per_update = parse_input(raw_input)
    results = [check_rules_per_update(pages_line, page_ordering) for pages_line in pages_per_update]
    print("Correct updates: ", sum(results))


