import random

from Card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        for value in range(1,14):
            for suit in range(1,4):
                self.cards.append(Card(value, suit))
    def draw(self, iteration):
        cards = []

        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards