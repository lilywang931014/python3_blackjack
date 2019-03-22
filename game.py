'''
Imports and Global Variable
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


'''
Class Definition
'''
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                newCard = Card(suit,rank)
                self.deck.append(newCard)

    def __str__(self):
        deck_com = ""
        for i in self.deck:
            deck_com = deck_com + i.__str__() + ","
        return deck_com
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return sincle_cards
