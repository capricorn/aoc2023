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
        
        print(results)
        
        w = [ r for r in results if r > dist ]
        print(w)
        winners.append(w)
    
    #print(winners)
    return prod([ len(w) for w in winners ])


print(p6p1())