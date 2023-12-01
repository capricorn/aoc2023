import re

def read_input():
    with open('p1.txt', 'r') as f:
        return [ line.strip() for line in f.readlines() ]

def part1():
    values = read_input()

    return sum(map(lambda f: int(f[0] + f[-1]), [ re.sub('[a-z]', '', val) for val in values ]))

def part2():
    values = read_input()

    new_values = []
    for val in values:
        n = extract(val)
        new_values.append(int(n[0] + n[-1]))
    
    return sum(new_values)

def extract(s):
    digit_matches = re.finditer('\d', s)
    words = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }

    word_matches = [ match for w in words.keys() for match in re.finditer(w,s) ]
    matches = sorted([*digit_matches, *word_matches], key=lambda k: k.start(0))

    return ''.join(map(lambda m: str(words[m.group(0)]) if m.group(0) in words else str(m.group(0)), matches))

if __name__ == '__main__':
    print(part1())
    print(part2())