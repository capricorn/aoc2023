import re

def read_input():
    with open('p1.txt', 'r') as f:
        return [ line.strip() for line in f.readlines() ]

def part1():
    values = read_input()

    print(sum(map(lambda f: int(f[0] + f[-1]), [ re.sub('[a-z]', '', val) for val in values ])))



def convert(val):
    words = [
        ('one', 1), ('two', 2), ('three', 3), ('four', 4), 
        ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine',9)
    ]

    words2 = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }


    def minmatch(s):
        matches = list(map(lambda f: f, filter(lambda f: f != None, [ re.search(w, s) for w,_ in words ] )))
        return None if matches == [] else min(matches, key=lambda f: f.start(0)).group(0)

    while (sub := minmatch(val)) != None:
        #print(sub, val)
        val = val.replace(sub, str(words2[sub]), 1)
        #print(val)

    val = re.sub('[a-z]', '', val)
    return val


def part2():
    # Problem: letters may overlap
    words = [
        ('one', 1), ('two', 2), ('three', 3), ('four', 4), 
        ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine',9)
    ]

    words2 = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }
    
    print(words)
    print(words2)

    values = read_input()
    print(len(values))
    #print('\n'.join(values))
    '''
    values = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]
    '''


    # How to fix:
    # eliminate any potential of substitution producing an invalid word.
    # Instead, find the min match, then search the remaining substring for the next min match.
    # **IMO: Don't use replace generically -- replace _exactly_ where the overlap happens.**
    # Otherwise perhaps replace is running in the wrong spot? 

    # edge case: substitution that results in a valid number _after_ the substitution? Is that possible?
    # example that's wrong: twoneeight -> 2oneight -> 21ight (nvm.. 2neeight)
    # twoneight -> 2neight -> 28
    # twonineightwo -> 292
    # nineightwone
    # eightwoneight -> 8woneight -> 
    # Above should actually be: 2ne8. (General form?)

    def minmatch(s):
        matches = list(map(lambda f: f, filter(lambda f: f != None, [ re.search(w, s) for w,_ in words ] )))
        return None if matches == [] else min(matches, key=lambda f: f.start(0)).group(0)
    
    # Alternative approach: assume that you _should_ match every occurrence, even overlapping.
    # (in order)
    # In that case, match all letters _and_ digits, sort by match



    # Shortcut:
    # If there is a num at end and beginning can just compute and skip
    # If not, find first num match on left and first match on right, sum those

    # Attempt at fixing problem
    #values = [ ''.join(reversed(v)) for v in values ]
    #words = [ (''.join(reversed(w)), num) for w, num in words ] 
    # eightwothree

    '''
    for w, num in words:
        print(w, num)
        values = [ re.sub(w, str(num), val) for val in values ]
    '''
    new_values = []
    for val in values:
        '''
        #print(val)
        initval = val
        while (sub := minmatch(val)) != None:
            #print(sub, val)
            val = val.replace(sub, str(words2[sub]), 1)
        #print(val)
        val = re.sub('[a-z]', '', val)

        result = int(val[0] + val[-1])
        print(f'{initval} -> {val} ({result})')
        #print(val)
        new_values.append(result)
        # Strip a-z here too
        #print(val)
        #print('')
        '''
        n = extract(val)
        new_values.append(int(n[0] + n[-1]))


        #print(val, minmatch(val))
    
    #print(new_values)
    print(sum(new_values))
    #values = new_values
    #print('\n'.join(values))
    #print([ re.sub('[a-z]', '', val) for val in values ])
    #print(sum(map(lambda f: int(f[0] + f[-1]), [ re.sub('[a-z]', '', val) for val in values ])))

def extract(s):
    digit_matches = re.finditer('\d', s)
    #return sorted(matches, key=lambda k: k.start(0))
    words = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }

    word_matches = [ match for w in words.keys() for match in re.finditer(w,s) ]

    matches = sorted([*digit_matches, *word_matches], key=lambda k: k.start(0))

    return ''.join(map(lambda m: str(words[m.group(0)]) if m.group(0) in words else str(m.group(0)), matches))

    #return sorted([*digit_matches, *word_matches], key=lambda k: k.start(0))


#print(extract('1213oneight'))
part2()
#part1()