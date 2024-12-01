# file_name = "test_input.txt"
file_name = "input.txt"

with open(file_name, "r") as f:
    lines = f.readlines()

col1, col2 = [], []
for line in lines:
    num1, num2 = line.split()
    col1.append(int(num1))
    col2.append(int(num2))

result = 0
for num in col1:
    result += num * col2.count(num)

print(result)