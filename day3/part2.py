import re

ex_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("input.txt", "r") as f:
    ex_input = f.read()

mul = lambda x, y: x * y
split_on_do = ex_input.split("do()")
split_on_dont_and_remove = [x.split("don't()")[0] for x in split_on_do]

print(sum([sum([eval(z) for z in re.findall(r"mul\(\d{1,3},\d{1,3}\)", x)]) for x in split_on_dont_and_remove]))
