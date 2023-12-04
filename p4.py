import re

def read_input(filename='p4.txt'):
    with open(filename, 'r') as f:
        return [ line.strip() for line in f.readlines() ]


def p4p1():
    cards = read_input(filename='p4.txt')
    ylen = 10

    card_tuples = list(map(lambda c: (c[1:ylen+1], c[ylen+1:]), [ re.findall('\d+', card) for card in cards ]))
    points = []
    for your_cards, winners in card_tuples:
        print(your_cards, winners, set(your_cards).intersection(set(winners)))
        # Are they always unique?
        matches = len(set(your_cards).intersection(set(winners)))
        points.append(0 if matches == 0 else 2**(matches-1))
        print(points[-1])

    return sum(points)

print(p4p1())