import random
from game_params import card_values, card_colors

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
def game():
    players_number = len(players)
    end_round = False
    dealer_indx = 0
    common_cards = []
    round_bets = {}
    current_max_bet = 0
    pot = 0

    def clear_bets():
        for player in players:
            round_bets[player.name] = 0

    clear_bets()

    for stage in range(0, 8):
        if end_round:
            break

        if stage == 0:
            deck = shuffle_deck(initial_deck)
            print('start deck', deck)

            for player in players:
                # Dealing players
                player.hand = deck[:2] # MAYBE keep hands in separate var?
                deck = deck[2:]
                print(f'{player.name} - {player.hand}')

                # Auto betting blinds
                player_indx = players.index(player)
                if player_indx == (dealer_indx + 1) % players_number:
                    round_bets[player.name] = small_blind
                    player.total_cash -= small_blind
                    pot += small_blind
                elif player_indx == (dealer_indx + 2) % players_number:
                    round_bets[player.name] = big_blind
                    player.total_cash -= big_blind
                    current_max_bet = big_blind
                    pot += big_blind
            
            common_cards = deck[:3]
            deck = deck[3:]
        
            print('bets:', round_bets)
            print('pot:', pot)
            print('common cards', common_cards)
            print('deck', deck)

        elif stage in [2, 4, 6]:
            for player in players:
                if round_bets[player.name] != -1:
                    round_bets[player.name] = 0

            # Dealing common cards
            common_cards.append(deck[0]) 
            deck = deck[1:]

            print('stage', stage)
            print('cards on table', common_cards)

        elif stage % 2 != 0:

            # while bets are not settled, repeat this stage
            # Players should be able to raise their bets mutltiple times

            if stage != 1:
                current_max_bet = 0 
            # Betting time
            settled = False
            while not settled:
                for player in players:
                    name = player.name
                    bet = round_bets[name]
                    if bet != -1:
                        call_bet = bet < current_max_bet # expand or move to if condition below
                        sum_to_call = current_max_bet - bet
                        print(f'{name}\'s turn')

                        print('bet', bet)
                        print('current max bet:', current_max_bet)

                        if call_bet:
                            print('[F]old / [C]all / [R]aise')
                        else:
                            print('[F]old / [C]heck / [B]et')
                        
                        action = input()
                        while action.upper() not in ['F', 'C', 'R', 'B']:
                            action = input()
                        if action.upper() == 'F':
                            round_bets[name] = -1

                            # See if every player but one (winner of the round) has folded
                            remaining_bets = 0
                            winner = None
                            for key in round_bets:
                                if round_bets[key] != -1:
                                    remaining_bets += 1
                                    winner = key
                            if remaining_bets == 1:
                                for player in players:
                                    if player.name == winner:
                                        player.total_cash += pot
                                        end_round = True

                        elif action.upper() == 'C':
                            if call_bet: # Player calls the bet
                                player.total_cash -= sum_to_call
                                round_bets[name] = current_max_bet
                                pot += sum_to_call
                            else: # Player checks
                                pass

                        elif action.upper() in ['R', 'B']:
                            print(f'Enter bet (0 - {player.total_cash}): ')
                            raising_with = int(input())
                            while raising_with <= 0 or raising_with > player.total_cash:
                                print('Invalid bet, try again.')
                                raising_with = int(input())
                            player.total_cash -= raising_with
                            round_bets[name] += raising_with
                            pot += raising_with
                            current_max_bet += raising_with
                # After all players have a round of bets, check if another round is needed or wagers are settled
                print('round_bets', round_bets)
                active_bets = filter(lambda bet: bet != -1, round_bets.values())
                unique_bets = set(active_bets)
                if len(unique_bets) == 1:
                    settled = True
                print('active_bets', active_bets)
                print('unique_bets', unique_bets)


# Test betting / raising more - see if biggest bet in a round is transferred in the next and that player shouldn't Call/Check it

game()