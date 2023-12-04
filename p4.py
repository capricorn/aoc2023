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

# Return all won cards -- once collected, run a counter (using set)
# This should just take a list of card tuples (and probably the assigned card num)
# The purpose is just to take a list of cards and expand them 
# pass a list of cards
# collect all subcards (via matches) of those
# specify the group too
def copy_cards(card_tuples, matched_cards):
    cards = []

    #for i, card_pack in enumerate(card_tuples):
    for card_id, your_cards, winners in matched_cards:
        card_id = int(card_id)
        won_cards = set(your_cards).intersection(set(winners))
        matches = len(won_cards)

        #card_num = i+1+offset
        # Always receive a single copy of the iterated card
        cards.append(str(card_id))
        #cards.extend(str(card_num))

        # TODO: Necessary?
        if matches == 0: continue

        # Given a card match, grab the next k cards
        #new_cards = list(map(str, range(card_id+1, card_id+matches+1)))
        #cards.extend(new_cards)
        #print(f'Card {card_id} matches: {matches} won: {new_cards}')
        # Grab the next 'matches' cards
        #print(f'Card id: {card_id} new cards: {new_cards}')
        cards.extend(copy_cards(card_tuples, card_tuples[card_id:card_id+matches]))
    
    return cards

def p4p2():
    cards = read_input(filename='p4.txt')
    ylen = 10

    counter = { str(card): 0 for card in range(0, 188) }

    card_tuples = list(map(lambda c: (c[0], c[1:ylen+1], c[ylen+1:]), [ re.findall('\d+', card) for card in cards ]))

    total_cards = copy_cards(card_tuples, card_tuples,)
    print(total_cards)
    '''
    for card in total_cards:
        counter[card] += 1

    print(counter)
    '''
    return len(total_cards)

    cards_won = set()
    points = []
    for i, card_pack in enumerate(card_tuples):
        your_cards, winners = card_pack
        #print(your_cards, winners, set(your_cards).intersection(set(winners)))

        matches = len(set(your_cards).intersection(set(winners)))
        # TODO: Bounds check? (According to rules, not necessary)
        #copied_cards = card_tuples[i+1: i+matches+1]
        copied_cards = []
        for copies in card_tuples[i+1: i+matches+1]:
            copied_cards.extend(copies[0])
        



        '''
        matches = len(set(your_cards).intersection(set(winners)))
        points.append(0 if matches == 0 else 2**(matches-1))
        print(points[-1])
        '''

    # TODO: Include original set of scratchcards (188?)
    return sum(points)

#print(p4p1())
print(p4p2())