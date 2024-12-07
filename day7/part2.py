from itertools import product
from typing import List, Tuple

def tri(n: int) -> str:
    # obviously taken from chatgpt, as long as it works XD
    if n == 0:
        return "0"
    base3 = ""

    while n > 0:
        base3 = str(n % 3) + base3
        n //= 3

    return base3

def get_input(test_input: bool = True) -> List[str]:
    file_name = "test_input.txt" if test_input else "input.txt"
    with open(file_name, "r") as f:
        return f.read().splitlines()


def parse_calibrations(calibrations: List[str]) -> List[Tuple[int, List[int]]]:
    result = []
    for calibration in calibrations:
        value, numbers = calibration.split(":")
        value = int(value)
        numbers = [int(num) for num in numbers.split()]
        result.append((value, numbers))
    return result


def calculate_operation(operations: str, num_list: List[int], expected: int) -> int:
    result = num_list[0]
    for i, operation in enumerate(operations):
        if result > expected:
            return False

        match operation:
            case "*":
                result *= num_list[i+1]
            case "+":
                result += num_list[i+1]
            case "|":
                result = int(str(result) + str(num_list[i+1]))
            case _:
                raise Exception("Unknown operation")

    return result == expected


def get_ops_from_num(op_idx: int, expected_len:int) -> str:
    op_tri = tri(op_idx)
    op_tri = op_tri.zfill(expected_len)
    op_translated = op_tri.replace("1", "*").replace("0", "+").replace("2", "|")
    return op_translated


def verify_can_be_calculated(calibration_line: Tuple[int, List[int]]) -> bool:
    expected_result, num_list = calibration_line
    print(f"Verifying {expected_result} can be obtained with {num_list}")
    op_len = len(num_list) - 1
    op_idx = 3**op_len - 1

    while op_idx >= 0:
        operations = get_ops_from_num(op_idx, op_len)
        if calculate_operation(operations, num_list, expected_result):
            print(f"Success with operations: {operations} for nums {num_list}")
            return True
        op_idx -= 1
    return False


if __name__ == '__main__':
    calibrations = get_input(True)
    print(parse_calibrations(calibrations))
    result = 0
    for calibration in parse_calibrations(calibrations):
        if verify_can_be_calculated(calibration):
            result += calibration[0]

    print(result)
