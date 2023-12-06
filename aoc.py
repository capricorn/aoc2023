from functools import reduce

# TODO: Optional chaining ideas

def flatten(lst):
    flattened = []
    
    for e in lst:
        if type(e) is list:
            flattened.extend(flatten(e))
        else:
            flattened.append(e)

    return flattened

def running_reduce(lst, f, initial=None):
    if initial:
        lst = [ initial, *lst ]
    
    return [ reduce(f, lst[:i+1]) for i in range(0, len(lst))]

def running_sum(lst):
    return running_reduce(lst, lambda a,b: a+b)

def compact_map(f, lst):
    return filter(lambda k: k != None, map(f, lst))

def fold(tree, f):
    return reduce(f, flatten(tree))

