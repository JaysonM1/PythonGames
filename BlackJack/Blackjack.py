from Deck import Deck
from Person import Player


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False,self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()

        self.player.show()

        if player_status == 1:
            print("Player got Blackjack. Congrats!")

            if dealer_status == 1:
                print("Dealer and player got BJ. Its a push")
            return 1

        cmd = ""
        while cmd != "Stand":
            bust = 0
            cmd = input("Hit or Stand? ")

            if cmd == "Hit":
                bust = self.play.hit()
                self.player.show()
            if bust == 1:
                print("Player busted")
                return 1
        print("\n")

        self.dealer.show()
        if dealer_status == 1:
            print("Dealer got blackjack")

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("It's a Push (Tie). Better luck next time!")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")

b = BlackJack()
b.play()