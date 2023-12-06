import re
from math import prod

def read_input(filename='p6.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]

def p6p1():
    puzzle = read_input()
    races = list(zip(re.findall('\d+', puzzle[0]), re.findall('\d+', puzzle[1])))

    winners = []
    for t, dist in races:
        t, dist = int(t), int(dist)
        d = lambda x, t1: max(0, t1*(x-t1)) # t1 is the total time held
        results = []
        for i in range(t+1):
            results.append(d(t, i))
        
        w = [ r for r in results if r > dist ]
        winners.append(w)
    
    return prod([ len(w) for w in winners ])

def p6p2():
    puzzle = read_input()
    race_time = int(''.join(re.findall('\d+', puzzle[0])))
    race_dist = int(''.join(re.findall('\d+', puzzle[1])))

    min_t = 0
    d = lambda x, t1: t1*(x-t1)
    while d(race_time, min_t) < race_dist:
        min_t += 1
    
    max_t = race_time
    while d(race_time, max_t) < race_dist:
        max_t -= 1

    return (max_t-min_t)+1

print(p6p1())
print(p6p2())