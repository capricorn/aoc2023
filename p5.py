def read_input(filename='p5.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]
    

def p5p1():
    puzzle = read_input()

def p5p2():
    ...

print(p5p1())