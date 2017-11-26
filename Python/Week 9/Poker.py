import random

class Card(object):
    rank = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    suit = ("Clubs", "Diamonds", "Hearts", "Spades")

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        prntStr = self.rank + self.suit
        return prntStr

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            prntStr = " "
            for card in self.cards:
                prntStr += str(card) + "  "
        else:
            prntStr = " empty "
        return prntStr

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)

class Deck(Hand):
    def __init__(self):
        self.cards = []

    def create(self):
        for suit in Card.suit:
            for rank in Card.rank:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def dealCards(self, hands, cardsPerHand):
        for rounds in range(cardsPerHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard, hand)
                else:
                    print("Can't deal, No more cards in deck!")

class Player(object):
    def __init__(self):
        self.playerHand = Hand()

class Game():
    def __init__(self):
        self.players = Player()
        self.numPlayers

    def intro(self):
        print("Welcome to Poker!\n")
        print("How many players do you wish to play with?\n")
        while True:
            try:
                self.numPlayers = input("Insert number here: ")
                break
            except ValueError:
                print("Numerical values only please.\n")
                continue

deck1 = Deck()
deck1.create()
print(deck1)
deck1.shuffle()
print(deck1)

playerOneHand = Hand()
playerTwoHand = Hand()
hands = [playerOneHand, playerTwoHand]
deck1.dealCards(hands, 5)

print("Dealt 5 cards to player one and player two.\n")
print("Player one hand: \n")
print(playerOneHand)
print("Player two hand: \n")
print(playerTwoHand)
print("Deck: \n")
print(deck1)
deck1.clear()
print("Cleared the deck. \n")
print("Deck: ", deck1)
input("Press the enter key to exit.\n")
