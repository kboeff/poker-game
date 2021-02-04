import random
from card import Card
from game_params import card_values, card_colors

class Deck:
    def __init__(self, values=None, colors=None):
        if values is None:
            self.values = card_values
        else:
            self.values = values
        if colors is None:
            self.colors = card_colors
        else:
            self.colors = colors

        self.deck = []
        for value in self.values:
            for color in self.colors:
                card = Card(value, color)
                self.deck.append(card)

    # Shuffle deck
    def shuffle(self):
        shuffled = self.deck
        random.shuffle(shuffled)
        self.deck = shuffled

    # Deal n cards
    def deal(self, n):
        cards = self.deck[:n]
        self.deck = self.deck[n:]
        return cards

    # Reset deck
    def reset(self):
        if self.values is None or self.colors is None:
            print('Error: Deck.reset() was called before initializing the deck.')
        else:
            self.deck = []
            for value in self.values:
                for color in self.colors:
                    card = Card(value, color)
                    self.deck.append(card)