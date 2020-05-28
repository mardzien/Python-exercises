""":argIn this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game.
Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits!
Remember to you are free to use any resources you want and as always:"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck(object):

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        last_card = self.deck.pop()
        return last_card


class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips(object):

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips: Chips):

    while True:
        try:
            chips.bet = int(input("How many chips would like to bet?"))
        except ValueError:
            print("A bet must be integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break


def show_some(player, dealer):

    print("Dealers hand:")
    print("one card hidden!")
    print(dealer.cards[1])
    print()
    print("Players hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    print("Dealers hand:")
    for card in dealer.cards:
        print(card)
    print()
    print("Players hand:")
    for card in player.cards:
        print(card)


def hit(deck: Deck, hand: Hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


def hit_or_stand(deck: Deck, hand: Hand):
    global playing

    while True:
        x = input("Hit or stand? Enter h or s") # h- hit, s- stand

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif [0].lower() == 's':
            print("Player stands. Dealer's turn")
            playing = False

        else:
            print("Please enter h or s only")

        break


def player_busts(player, dealer, chips):
    print("Bust player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player wins, dealer busted!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie!")


if __name__ == "__main__":

    while True:
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)
