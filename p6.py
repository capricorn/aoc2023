def read_input(filename='p6.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]

def p6p1():
    puzzle = read_input()

print(p6p1())