import re


def get_variables(text):
    vars = re.findall(r'([\w\d]+)(?=(( =)|(,)))', text)
    return list(map(itemgetter(0)))


filename = 'A.py'
with open(filename, 'r') as f:
    vars = []
    for line in f.readlines():
        vars += get_variables(line)
    print(vars)
