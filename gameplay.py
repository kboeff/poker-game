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

test_players = [
    ('boba', 1000),
    ('booba', 2000),
    ('bebop', 2000),
    ('abba', 2000),
    ('boabab', 2000),
    ('bae', 1000)
]

# Declaring input variables with some initial values
small_blind = 5
big_blind = 10

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
    def __init__(self, name, total_cash):
        self.total_cash = total_cash
        self.name = name

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{self.name} ${self.total_cash}'

# Init deck 
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

# Init players
def make_player(name_cash):
    return Player(name_cash[0], name_cash[1])
players = list(map(make_player, test_players)) # use list comprehention insted and add index
print('players:', players)

# Game loop
players_number = len(players)
stage = 0
dealer_indx = 0
bets_on_table = [0 for indx in range(players_number)]
common_cards = []

while stage != -1:

    if stage == 0:
        deck = shuffle_deck(initial_deck)
        print('start deck', deck)

        for player in players:
            # Dealing players
            player.hand = deck[:2] # MAYBE keep hands in separate var?
            deck = deck[2:]

            # Auto betting blinds
            player_indx = players.index(player)
            if player_indx == (dealer_indx + 1) % players_number:
                bets_on_table[player_indx] += small_blind
                player.total_cash -= small_blind
            elif player_indx == (dealer_indx + 2) % players_number:
                bets_on_table[player_indx] += big_blind
                player.total_cash -= big_blind
        
        common_cards = deck[:3]
        deck = deck[3:]
    
        print('Players', players)
        print('bets:', bets_on_table)
        print('common cards', common_cards)
        print('deck', deck)
        stage = -1