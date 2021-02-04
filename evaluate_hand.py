from collections import Counter
from game_params import poker_scores, card_values, card_colors
from deck import Deck

from card import Card

test_deck = Deck()
test_deck.shuffle()
test_hands = [test_deck.deal(5) for i in range(0,5)]

test_straight = [{ 'value': '4', 'color': 'S' },{ 'value': '5', 'color': 'S' },{ 'value': '6', 'color': 'S' },{ 'value': '7', 'color': 'S' },{ 'value': '8', 'color': 'S' }]
test_str_cards = [Card(card['value'], card['color']) for card in test_straight]


print(test_hands)

# Helper functions
# Get occurances of card values in a list
def get_counts(hand):
    card_values = [card.value for card in hand]
    return [card_values.count(value) for value in card_values]

# Boolean checks for different hands
def high_card(hand):
    counts = get_counts(hand)
    return counts.count(1) == 5

def two_pairs(hand):
    counts = get_counts(hand)
    return counts.count(2) == 4    

def n_of_a_kind(hand, n):
    card_values = [card.value for card in hand]
    for value in card_values:
        if card_values.count(value) == n:
            return True
    return False

def straight(hand):
    straight_cards = card_values
    if card_values[-1] == 'A':
        straight_cards = ['A'] + straight_cards
    indexes = [straight_cards.index(card.value) for card in hand]
    indexes.sort()
    counts = [indexes.count(i) for i in indexes]
    return not (counts.count(1) != 5 or max(indexes) - min(indexes) != 4)
    
def full_house(hand):
    counts = get_counts(hand)
    return (counts.count(3) == 3 and counts.count(2) == 2)

# def score_hand(hand):
#     counts = Counter(map(lambda card: card.value, hand))
#     max_repeated = None
    # for count in counts:
    #     if count:
    #         return 1