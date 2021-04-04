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
class Hand_Checks:    
    def high_card(self, hand):
        counts = get_counts(hand)
        return counts.count(1) == 5

    def two_pairs(self, hand):
        counts = get_counts(hand)
        return counts.count(2) == 4

    def n_of_a_kind(self, hand, n):
        card_values = [card.value for card in hand]
        for value in card_values:
            if card_values.count(value) == n:
                return True
        return False

    def straight(self, hand):
        straight_cards = card_values
        if card_values[-1] == 'A':
            straight_cards = ['A'] + straight_cards
        indexes = [straight_cards.index(card.value) for card in hand]
        indexes.sort()
        counts = [indexes.count(i) for i in indexes]
        return not (counts.count(1) != 5 or max(indexes) - min(indexes) != 4)
        
    def full_house(self, hand):
        counts = get_counts(hand)
        return (counts.count(3) == 3 and counts.count(2) == 2)

    def pair(self, hand):
        return self.n_of_a_kind(hand, 2)

    def three_of_a_kind(self, hand):
        return self.n_of_a_kind(hand, 3)

    def four_of_a_kind(self, hand):
        return self.n_of_a_kind(hand, 4)

    def flush(self, hand):
        colors = [card.color for card in hand]
        return (colors.count(colors[0]) == 5)

    def straight_flush(self, hand):
        return (self.straight(hand) and self.flush(hand))


def get_hand_max_score(hand, scores):
    all_checks = [scores[key] if Hand_Checks[key](hand) else 0 for key in scores]
    return max(all_checks)
