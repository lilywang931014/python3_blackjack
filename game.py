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
        return single_cards

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

def show_some(player,dealer):

    print("Dealer's hand")
    print("<card hidden>")
    print("", dealer.card[1])
    print("\nPlayer's hand :", *player.cards, sep="\n")

def show_all(player,dealer):

    print("Dealer's hand: " ,*dealer.cards, sep = "\n")
    print("\nDealer's hand = " + dealer.value )
    print("\nPlayer's hand :", *player.cards, sep="\n")
    print("\nPlayer's hand = " + player.value)

while True:
    # Print an opening statement
    print("Opening the Game!")


    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    # Set up the Player's chips
    player_chips = Chip()


    # Prompt the Player for their bet
    take__bet(player_chips)


    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)


        # Show cards (but keep one dealer card hidden)
        show_some(deck,dealer_hand)


        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts()
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_value > 21:
            dealer_bust(player_hand,dealer_hand,dealer_chips)
        elif dealer_value > player_value:
            dealer_wins(player_hand,dealer_hand,dealer_chips)
        elif dealer_value < player_value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_value == player_valuer:
            push()


    # Inform Player of their chips total
    print("Player's chips: " + player_chips.total)
    print("Dealer's chips: " + dealer_chips.total)

    # Ask to play again
    answer = input("Do you wanna play it again?")
    if answer[0].lower() == "y":
        playing = True
        continue
    elif answer[0].lower() == "n":
        playing == False
        break
