# file_name = "test_input.txt"
file_name = "input.txt"

with open(file_name, "r") as f:
    lines = f.readlines()

col1, col2 = [], []
for line in lines:
    num1, num2 = line.split()
    col1.append(int(num1))
    col2.append(int(num2))

col1.sort()
col2.sort()
result = sum([abs(x-y) for x,y in zip(col1, col2)])
print(result)