import re
#from math import prod

def read_input(filename='p3.txt'):
    with open(filename, 'r') as f:
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

def p3p2():
    col=140
    puzzle = [ '.'*col, *read_input(), '.'*col ]

    parts = []
    for i in range(1, len(puzzle)-1):
        top = re.finditer('\d+', puzzle[i-1])
        middle = re.finditer('\d+', puzzle[i])
        bottom = re.finditer('\d+', puzzle[i+1])

        adj = [ *top, *middle, *bottom ]
        stars = re.finditer('\*', puzzle[i])

        for star in stars:
            star_start, star_end = star.start(0), star.end(0)

            matches = []
            for adj_match in adj:
                adj_start, adj_end = adj_match.start(0), adj_match.end(0)
                if star_start >= adj_start-1 and star_end <= adj_end+1:
                    matches.append(int(adj_match.group(0)))
            
            if len(matches) >= 2:
                parts.append(matches)

    return sum([ p1*p2 for p1,p2 in parts ])

print(p3p2())