import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

class BlackjackGame:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        self.players = players
        self.scores = {}
        print("Created a game with {} players.".format(len(self.players)))
players=BlackjackGame()
def blackjack(self):

    print("Setting up...")
    print("Shuffling...")
    self.deck.shuffle()
    print("All shuffled!")
    print("Dealing...")
    self.deal()
    print("\nLet's play!")
    for player in self.players:
        print("{}'s turn...".format(player.name))
        self.play(player)
    else:
        print("That's the last turn. Determining the winner...")
self.find_winner()
