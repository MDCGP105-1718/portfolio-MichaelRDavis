import random

# Our card
class Card(object):
    def __init__(self, Rank, Suit):
        self.Rank = Rank
        self.Suit = Suit

    Rank = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
    Suit = ("Spades", "Diamonds", "Hearts", "Clubs")

# Our deck of cards
class Deck(object):
    def __init__(self):
        self.Deck = []
        for suit in Card.Suit:
            for rank in Card.Rank:
                card = Card(Rank, Suit)
                self.Deck.append(card)

    def suffleDeck(self):
        random.shuffle(self.Deck)

# Our hand we are dealt
class Hand():
    def __init__(self):
        self.Deck = Deck()
        self.Deck.shuffle()
        self.Hands = []
        self.MaxHand = 5

    def FiveOfAKind(self):
        print("Five of a Kind")

    def StraightFlush(self):
        print("Straight Flush")

    def FourOfAKind(self):

        print("Four of a Kind")

    def FullHouse(self):
        print("Full House")

    def Flush(self):
        print("Flush")
        flushSuit = self.Hands.Suit
        for cards in self.Hands:
            if cards.Suit != flushSuit:
                print("This hand is not a Flush\n")
                return False
            else:
                flushSuit = cards.Suit
                print("This hand is a Flush!\n")
                return True

    def Straight(self):
        print("Straight")

    def ThreeOfAKind(self):
        print("Three of a Kind")

    def TwoPair(self):
        print("Two Pair")

    def OnePair(self):
        print("One Pair")

    def HighCard(self):
        print("High Card")

    def GetHand(self):
        return Hands

# The player class, each player is dealt a hand
class Player():
    def __init__(self):
        self.players = 0
        self.maxPlayers = 4

    def getNumPlayers(self):
        while True:
            try:
                self.players = int(input("Insert the number of players you want to play Poker with.\n "))
                if self.players > self.maxPlayers:
                    print("There are two many players, this Poker Torunament can only support four players!\n")
                    continue
                else:
                    print("Press enter to deal the cards to each player!\n")
                    break
            except ValueError:
                print("Not a numerical value, please try agian\n")
                continue

# The game of poker that we play
class PokerGame():
    def __init__(self):
        self.players = Player()
        self.hands = Hand()

    def play(self):
        print("Welcome to the Python Poker Tournament!\n")
        self.players.getNumPlayers()
        self.dealHands()

    def dealHands(self):
        for player in self.players.getNumPlayers():
            dealtHand = self.hands.GetHand()

# Start our poker game
poker = PokerGame()
poker.play()
