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

def indices(lst, val):
    if len(lst) == 0:
        return []

    try:
        idx = lst.index(val)
    except ValueError:
        return []

    return flatten([idx, indices(lst[idx+1:], val)])

def swap(lst, a, b):
    if (0 < a > len(lst)) or (0 < b > len(lst)):
        raise ValueError
    
    lst = [ *lst ]
    copy = lst[a]
    lst[a] = lst[b]
    lst[b] = copy

    return lst

def apply_k(f, k, initial):
    counter = 0
    def pred(val):
        nonlocal counter
        result = counter < k
        counter += 1
        return result
    
    return apply_while(f, pred, initial=initial)

def apply_while(f, pred, initial):
    result = initial
    while pred(result):
        result = f(result)
    
    return result