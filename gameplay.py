import random

# Defining input constants
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_colors = ['S', 'H', 'D', 'C']
poker_scores = {
    'high_card': 1,
    'pair': 2,
    'two_pairs': 3,
    'three_of_a_kind': 4,
    'straignt': 5,
    'flush': 6,
    'full_house': 7,
    'four_of_a_kind': 8,
    'straight_flush': 9 
}

# Declaring input variables with some initial values
players_number = 0
small_blind = 0
big_blind = 0

# Card class
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.value}{self.color}'


# Player class
class Player:
    def __init__(self, total_cash, current_bet, hand):
        self.total_cash: total_cash
        self.current_bet: current_bet
        self.hand: hand

# Deck 
def build_deck(card_values, card_colors):
    deck = []
    for value in card_values:
        for color in card_colors:
            card = Card(value, color)
            deck.append(card)
    return deck

initial_deck = build_deck(card_values, card_colors)
print('Initial deck:', initial_deck)

# Shuffle deck
def shuffle_deck(deck):
    shuffled = deck
    random.shuffle(shuffled)
    return shuffled

print('Shuffled:', shuffle_deck(initial_deck))


# Deal

# Evaluate hand function

# Game loop

