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
        matches = len(set(your_cards).intersection(set(winners)))
        points.append(0 if matches == 0 else 2**(matches-1))

    return sum(points)

def copy_cards(card_tuples, matched_cards):
    cards = []

    for card_id, your_cards, winners in matched_cards:
        card_id = int(card_id)
        won_cards = set(your_cards).intersection(set(winners))
        matches = len(won_cards)

        cards.append(str(card_id))
        if matches == 0: continue

        cards.extend(copy_cards(card_tuples, card_tuples[card_id:card_id+matches]))
    
    return cards

def p4p2():
    cards = read_input(filename='p4.txt')
    ylen = 10

    card_tuples = list(map(lambda c: (c[0], c[1:ylen+1], c[ylen+1:]), [ re.findall('\d+', card) for card in cards ]))

    total_cards = copy_cards(card_tuples, card_tuples,)
    return len(total_cards)

print(p4p1())
print(p4p2())