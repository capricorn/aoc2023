import re

def read_input():
    with open('p3.txt', 'r') as f:
        return [ line.strip() for line in f.readlines() ]
    
def p3p1():
    col=140
    puzzle = [ '.'*col, *read_input(), '.'*col ]

    parts = []
    for i in range(1, len(puzzle)-1):
        top = re.finditer('\W', puzzle[i-1].replace('.', '_'))
        middle = re.finditer('\W', puzzle[i].replace('.', '_'))
        bottom = re.finditer('\W', puzzle[i+1].replace('.', '_'))
        adj = [ *top, *middle, *bottom ]

        numbers = re.finditer('\d+', puzzle[i])

        for num_match in numbers:
            start, end = num_match.start(0), num_match.end(0)
            if len(list(filter(lambda t: t.start(0) >= start-1 and t.end(0) <= end+1, adj))) > 0:
                # This is a part number
                parts.append(int(num_match.group(0)))
    
    return sum(parts)

print(p3p1())