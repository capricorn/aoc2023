from functools import reduce

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

# TODO: Optional chaining ideas