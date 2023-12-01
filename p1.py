import re

def part1():
    with open('p1.txt', 'r') as f:
        values = [ line.strip() for line in f.readlines() ]

    print(sum(map(lambda f: int(f[0] + f[-1]), [ re.sub('[a-z]', '', val) for val in values ])))

