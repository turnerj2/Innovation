"""
Defines a class to represent a Deck of cards.
"""

"""
Import necessary packages.
"""

from random import shuffle

"""
Defines the Deck class.
"""


class Deck:
    """
    Class to represent a deck of cards.
    """

    def __init__(self, num=0, cards=None):
        """
        Deck will be a list of cards.
        """

        self.num = num
        self.cards = cards if cards is not None else []


    def __str__(self):
        """
        Cards in deck will be printed in order.
        """

        for card in self.cards:
            print(card)

        return ("~~~~~~~~")

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """

        cards = self.cards[:]
        shuffle(cards)
        self.cards = cards

    def meld(self, board, name):
        """
        Meld a card onto a board.
        """

        deck_list = {card.name: card for card in self.cards}

        to_meld = deck_list.pop(name)

        if to_meld.color == 'red':
            board.red.cards.insert(0, to_meld)
        elif to_meld.color == 'yellow':
            board.yellow.cards.insert(0, to_meld)
        elif to_meld.color == 'green':
            board.green.cards.insert(0, to_meld)
        elif to_meld.color == 'blue':
            board.blue.cards.insert(0, to_meld)
        elif to_meld.color == 'purple':
            board.purple.cards.insert(0, to_meld)
        else:
            print("ERROR")

        self.cards = list(deck_list.values())

        print("You have melded {} onto your board!".format(name))

    def tuck(self, board, name):
        """
        Tuck a card onto a board.
        """

        deck_list = {card.name: card for card in self.cards}

        to_meld = deck_list.pop(name)

        if to_meld.color == 'red':
            board.red.cards.append(to_meld)
        elif to_meld.color == 'yellow':
            board.yellow.cards.append(to_meld)
        elif to_meld.color == 'green':
            board.green.cards.append(to_meld)
        elif to_meld.color == 'blue':
            board.blue.cards.append(to_meld)
        elif to_meld.color == 'purple':
            board.purple.cards.append(to_meld)
        else:
            print("ERROR")

        self.cards = list(deck_list.values())

        print("You have tucked {} onto your board!".format(name))

    def re_turn(self, collection, name):
        """
        Return a card to the collection of subpile.
        """

        deck_list = collection.decks[:]
        cards = self.cards[:]
        to_return = cards.pop(name)

        i = to_return.num
        deck_list[i].append(to_return)

        collection.decks = deck_list
        self.cards = cards

        print("You have returned {} to the suply piles!".format(name)) # Working on this