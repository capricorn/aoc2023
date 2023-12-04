def read_input(filename='p4.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]

