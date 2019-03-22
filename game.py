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

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values.get(card.rank)

    def adjust_for_ace(self):
        while self.value >= 21 and self.aces:
            self.values -= 10
            self.aces -1

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

'''
Function Definition
'''

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much you wanna bet? "))
        except:
            print("Value is unavailable! ")
            continue
        else:
            if chips.bet > chips.total:
                print("You don't have enough!")
                continue
            else:
                print("Successful")
                break


def hit(deck,hand):
    hand.add_card(deck.deal)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while playing:
        x = input("Hit or Stand: ")
        if x[0].lower() == "h":
            hit(deck,hand)
        elif x[0].lower() == "s":
            playing = False
        else:
            x = input("input invalid! please enter again!")
            continue
        
