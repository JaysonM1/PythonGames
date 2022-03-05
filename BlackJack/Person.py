from Deck import Deck

class Player:
    def __init__(self, isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.deck = deck
        self.hand = 0


    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        if self.hand > 21:
            return 1
        else:
            return 0

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.check_score()
        if self.hand == 21:
            return 1
        return self.hand

    def check_score(self):
        counter = 0
        self.hand = 0
        for card in self.cards:
            if card.price() == 11:
                counter += 1
            self.hand += card.price()

        while counter != 0 and self.hand() > 21:
            counter -= 1
            self.hand -= 11
        return self.hand


    def show(self):
        if self.isDealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for i in self.cards:
            i.show()

        print("Score: " + str(self.hand))

