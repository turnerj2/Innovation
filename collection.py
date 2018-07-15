"""
Defines a class for a grouping of Decks.
"""

"""
Import necessary packages.
"""

from random import shuffle

"""
Defines the Collection class.
"""


class Collection:
    """
    Class for a collection of decks.
    """

    def __init__(self, decks):
        """
        A collection is a list of decks.
        """

        self.decks = decks

    def __str__(self):
        """
        Decks in collection will be printed with deck number.
        """

        for deck in self.decks:
            print("Deck number: {}".format(deck.num))
            print(deck)

        return ("-------")

    def draw(self, i, hand, n):
        """
        Draws n cards from the ith deck and puts them in the hand.
        """

        decks = self.decks[:]
        deck_cards = decks[i].cards
        j = 0

        while j < n and len(deck_cards) > 0:
            drawn_card = deck_cards.pop(0)
            hand.cards.append(drawn_card)
            j += 1

        if j < n and not deck_cards:
            if i < len(self.decks) - 1:
                print("Deck {} is out of cards, drawing from deck {}.".format(i, i + 1))
                self.draw(i + 1, hand, n - j)

            else:
                print("Out of decks!")

        self.cards = deck_cards
