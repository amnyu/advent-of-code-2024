from typing import List
import inflect


def verify_report_safety(report_diffs_list: List[int]) -> bool:
    if all(map(lambda x: x > 0, report_diffs_list)) or all(map(lambda x: x < 0, report_diffs_list)):
        if all(map(lambda x: abs(x) <= 3, report_diffs_list)):
            return True

    return False

def verify_reports(reports: List[List[int]]):
    result_plain = 0
    result_dampened = 0
    p = inflect.engine()

    for row in reports:
        diff_list = [int(row[i]) - int(row[i - 1]) for i in range(1, len(row))]
        if verify_report_safety(diff_list):
            result_plain += 1
            continue
        else:
            sep = "\t" * int(9 - len(str(row))//4)
            for i in range(len(row)):
                shortened_row = row.copy()
                shortened_row.pop(i)
                diff_list = [int(shortened_row[i]) - int(shortened_row[i - 1]) for i in range(1, len(shortened_row))]
                if verify_report_safety(diff_list):
                    print(f"{row}{sep}: Safe by removing {p.ordinal(i+1)} level, {row[i]}")
                    result_dampened += 1
                    break
                if i == len(row)-1:
                    print(f"{row}{sep}: Unsafe regardless of which level is removed")
            continue

        # print(diff_list)
    result = result_plain + result_dampened
    print("*" * 81)
    print(f"Plain passing reports: {result_plain}")
    print(f"Dampened passing result: {result_dampened}")
    print(f"Result: {result}")

if __name__ == '__main__':
    file_name = "input.txt"
    # file_name = "test_input.txt"

    with open(file_name, "r") as f:
        rows = f.readlines()
        rows = [row.strip() for row in rows]
        rows = [[int(num) for num in row.split()] for row in rows]

    verify_reports(rows)
