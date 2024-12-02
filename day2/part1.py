#file_name = "test_input.txt"
file_name = "input.txt"

with open(file_name, "r") as f:
    rows = f.readlines()

rows = [[int(num) for num in row.split()] for row in rows]
result = 0

for row in rows:
    diff_list = [int(row[i]) - int(row[i - 1]) for i in range(1, len(row))]
    if all(map(lambda x: x > 0, diff_list)) or all(map(lambda x: x < 0, diff_list)):
        if all(map(lambda x: abs(x) <= 3, diff_list)):
            result += 1

print(result)
