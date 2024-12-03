import re
ex_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open("input.txt", "r") as f:
    ex_input = f.read()

mul = lambda x,y: x*y
print(sum([eval(x) for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)", ex_input)]))