import re

# ex_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("input.txt", "r") as f:
    ex_input = f.read()

mul = lambda x, y: x * y

# finding sections matching start-don't | do-don't | do-end
do_sections = re.findall(r"(?:(?<=do\(\))|(?<=^))[\s\S]+?(?:(?=don't\(\))|(?=$))", ex_input)
# getting mul statements for each section
mul_statements = [re.findall(r"mul\(\d{1,3},\d{1,3}\)", section) for section in do_sections]

# funny way to flatten the list of lists (lists of mul statements per each section)

print(sum(eval(x) for x in sum([single_mul for single_mul in mul_statements], start=[])))

# Old answer, also worked fine but took too much time with regex so had to have a partial win
# split_on_do = ex_input.split("do()")
# split_on_dont_and_remove = [x.split("don't()")[0] for x in split_on_do]
#
# print(sum([sum([eval(z) for z in re.findall(r"mul\(\d{1,3},\d{1,3}\)", x)]) for x in split_on_dont_and_remove]))
