import re
import math

def read_input():
    with open('p2.txt', 'r') as f:
        return [ line.strip() for line in f.readlines() ]

def p2p2():
    input = read_input()
    cubes = []
    limits = [('red',12), ('green', 13), ('blue', 14)]

    for game in input:
        draws = game.split(';')

        min_colors = { 'red': 0, 'blue': 0, 'green': 0}
        for color, _ in limits:
            color_draws = list(map(lambda d: int(d.group(1)), filter(lambda d: d != None, [ re.search(f'(\d+) {color}', g) for g in draws ])))
            color_draws.append(0)
            min_colors[color] = max(color_draws)
        
        cubes.append(math.prod(min_colors.values()))
        
    return sum(cubes)

def p2p1():
    input = read_input()

    possible_ids = []
    limits = [('red',12), ('green', 13), ('blue', 14)]
    for game in input:
        game_id = int(re.match('Game (\d+)', game).group(1))
        draws = game.split(';')

        accept = True
        for color, color_max in limits:
            color_draws = list(map(lambda d: int(d.group(1)), filter(lambda d: d != None, [ re.search(f'(\d+) {color}', g) for g in draws ])))
            color_draws.append(0)
            #print(color_draws)
            if len(list(filter(lambda r: r > color_max, color_draws ))) > 0:
                accept = False
                break
        
        if accept:
            possible_ids.append(game_id)

    
    return sum(possible_ids)

if __name__ == '__main__':
    print(p2p1())
    print(p2p2())