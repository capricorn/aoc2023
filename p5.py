import re
from collections import OrderedDict
from functools import reduce

def read_input(filename='p5.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]
    
def resolve(selector, mapping, num):
    block = mapping[selector]
    for entry in block:
        if num >= entry['src'] and num <= entry['src'] + entry['range']:
            return (num - entry['src']) + entry['dst']
    
    return num

def p5p1():
    puzzle = read_input()
    # Seed numbers -- want to convert to a location number
    seeds = re.findall('\d+', puzzle[0])

    print(seeds)
    print(puzzle)

    offsets = [*[ i+1 for i, val in enumerate(puzzle) if val == ''], len(puzzle)+1]
    #print(offsets)
    blocks = [ puzzle[start:end-1] for start, end in zip(offsets, offsets[1:])] 
    print(blocks)
    block_tuple =  lambda b: {'dst': int(b.split(' ')[0]), 'src': int(b.split(' ')[1]), 'range': int(b.split(' ')[2]) }
    blocks = OrderedDict({ block[0].split(' ')[0]: list(map(block_tuple, block[1:])) for block in blocks })
    print(blocks)

    print(blocks.keys())

    #for key in blocks.keys():
    #    print(key)
    #return min([ reduce(lambda prev, curr: resolve(), seed) for seed in seeds ])
    results = [ reduce(lambda prev, curr: resolve(curr, blocks, prev), blocks.keys(), int(seed)) for seed in seeds ]
    print(results)
    return min(results)

    '''
    blocks.keys
    return min([
        resolve('humidity-to-location', blocks,
                resolve('temperature-to-humidity', blocks,
                        resolve('light-to-temperature', blocks,
                                resolve('water-to-light', blocks,
                                        resolve('fertilizer-to-water')))))
    ])
    '''

    #print(blocks)
    '''
    for block in blocks:
        print(block)
    '''



    # Next, split maps

def p5p2():
    ...

print(p5p1())